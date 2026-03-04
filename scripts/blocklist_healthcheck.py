#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import List, Optional, Tuple
from urllib.parse import urlparse

import requests


LINK_MD_RE = re.compile(r"\[link\]\((https://[^)]+)\)", re.IGNORECASE)
RAW_HTTPS_RE = re.compile(r"(https://[^\s)]+)")
USER_AGENT = "PrimePoobah-BlocklistHealthcheck/1.0 (+https://github.com/PrimePoobah/Pi-hole-Blocklist-Catalog)"


@dataclass
class Result:
    url: str
    final_url: Optional[str]
    status_code: Optional[int]
    ok: bool
    method: Optional[str]
    elapsed_ms: Optional[int]
    last_modified: Optional[str]
    etag: Optional[str]
    content_type: Optional[str]
    content_length: Optional[int]
    error: Optional[str]


def is_https(url: str) -> bool:
    try:
        return urlparse(url).scheme.lower() == "https"
    except Exception:
        return False


def extract_urls(markdown_text: str) -> List[str]:
    urls: List[str] = []

    # Prefer [link](https://...) style
    urls.extend(LINK_MD_RE.findall(markdown_text))

    # Also catch raw https URLs if any slipped in
    urls.extend(RAW_HTTPS_RE.findall(markdown_text))

    # De-dup while preserving order
    seen = set()
    cleaned = []
    for u in urls:
        u = u.strip().rstrip(".,;")
        if u not in seen:
            seen.add(u)
            cleaned.append(u)
    return cleaned


def try_head_then_get(
    url: str,
    timeout: int,
    max_redirects: int,
    session: requests.Session,
) -> Result:
    if not is_https(url):
        return Result(
            url=url,
            final_url=None,
            status_code=None,
            ok=False,
            method=None,
            elapsed_ms=None,
            last_modified=None,
            etag=None,
            content_type=None,
            content_length=None,
            error="non-https url (rejected)",
        )

    headers = {"User-Agent": USER_AGENT}
    start = time.time()

    def mk_result(
        ok: bool,
        method: str,
        resp: Optional[requests.Response] = None,
        error: Optional[str] = None,
        status_code: Optional[int] = None,
    ) -> Result:
        elapsed_ms = int((time.time() - start) * 1000)
        if resp is None:
            return Result(
                url=url,
                final_url=None,
                status_code=status_code,
                ok=ok,
                method=method,
                elapsed_ms=elapsed_ms,
                last_modified=None,
                etag=None,
                content_type=None,
                content_length=None,
                error=error,
            )
        lm = resp.headers.get("Last-Modified")
        etag = resp.headers.get("ETag")
        ct = resp.headers.get("Content-Type")
        cl = resp.headers.get("Content-Length")
        cl_int = None
        if cl is not None:
            try:
                cl_int = int(cl)
            except Exception:
                cl_int = None

        return Result(
            url=url,
            final_url=str(resp.url),
            status_code=int(resp.status_code),
            ok=ok,
            method=method,
            elapsed_ms=elapsed_ms,
            last_modified=lm,
            etag=etag,
            content_type=ct,
            content_length=cl_int,
            error=error,
        )

    # HEAD attempt
    try:
        resp = session.head(
            url,
            headers=headers,
            timeout=timeout,
            allow_redirects=True,
        )
        # Some servers refuse HEAD with 403/405 even though GET works
        if resp.status_code in (403, 405):
            raise requests.HTTPError(f"HEAD not allowed: {resp.status_code}")

        ok = 200 <= resp.status_code < 400
        return mk_result(ok=ok, method="HEAD", resp=resp)

    except Exception as e:
        # GET fallback (stream to avoid downloading huge lists)
        try:
            resp = session.get(
                url,
                headers=headers,
                timeout=timeout,
                allow_redirects=True,
                stream=True,
            )
            ok = 200 <= resp.status_code < 400
            # read tiny amount to ensure connection actually works
            try:
                next(resp.iter_content(chunk_size=4096), b"")
            except Exception:
                pass
            return mk_result(ok=ok, method="GET", resp=resp)
        except Exception as e2:
            return mk_result(
                ok=False,
                method="GET",
                resp=None,
                error=f"{type(e2).__name__}: {e2}",
            )


def render_report_md(results: List[Result], generated_at: str) -> str:
    total = len(results)
    down = [r for r in results if not r.ok]
    up = [r for r in results if r.ok]

    lines = []
    lines.append(f"# Blocklist Healthcheck Report")
    lines.append("")
    lines.append(f"- Generated: **{generated_at}**")
    lines.append(f"- Total URLs checked: **{total}**")
    lines.append(f"- Reachable: **{len(up)}**")
    lines.append(f"- Unreachable: **{len(down)}**")
    lines.append("")

    if down:
        lines.append("## ❌ Unreachable / Failed")
        lines.append("")
        lines.append("| URL | Status | Method | Last-Modified | ETag | Error |")
        lines.append("|-----|--------|--------|---------------|------|-------|")
        for r in down:
            status = str(r.status_code) if r.status_code is not None else "—"
            lm = r.last_modified or "—"
            et = (r.etag or "—").replace("|", "\\|")
            err = (r.error or "—").replace("|", "\\|")
            lines.append(f"| {r.url} | {status} | {r.method or '—'} | {lm} | {et} | {err} |")
        lines.append("")

    lines.append("## ✅ Reachable")
    lines.append("")
    lines.append("| URL | Final URL | Status | Method | Last-Modified | ETag | Content-Type |")
    lines.append("|-----|----------|--------|--------|---------------|------|-------------|")
    for r in up:
        status = str(r.status_code) if r.status_code is not None else "—"
        lm = r.last_modified or "—"
        et = (r.etag or "—").replace("|", "\\|")
        ct = (r.content_type or "—").split(";")[0]
        final = r.final_url or "—"
        lines.append(f"| {r.url} | {final} | {status} | {r.method or '—'} | {lm} | {et} | {ct} |")

    lines.append("")
    lines.append("### Notes")
    lines.append("- Some providers do not return `Last-Modified` or `ETag`. That is not a failure by itself.")
    lines.append("- Some providers block `HEAD`; this checker automatically falls back to `GET`.")
    lines.append("- If a list is consistently unreachable, consider mirroring it in your own repo for stability.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True, help="Path to BLOCKLIST_CATALOG.md")
    ap.add_argument("--out-md", required=True, help="Output markdown report path")
    ap.add_argument("--out-json", required=True, help="Output JSON report path")
    ap.add_argument("--timeout", type=int, default=12, help="Timeout in seconds")
    ap.add_argument("--max-redirects", type=int, default=5, help="Max redirects (requests handles this internally)")
    ap.add_argument("--fail-on-down", action="store_true", help="Exit non-zero if any URL is unreachable")
    ap.add_argument("--sleep-ms", type=int, default=150, help="Delay between requests (polite throttling)")
    args = ap.parse_args()

    with open(args.catalog, "r", encoding="utf-8") as f:
        text = f.read()

    urls = extract_urls(text)
    # Keep only HTTPS; report non-HTTPS as failures
    urls = urls  # already filtered later

    session = requests.Session()
    session.max_redirects = args.max_redirects

    results: List[Result] = []
    for url in urls:
        r = try_head_then_get(url, args.timeout, args.max_redirects, session)
        results.append(r)
        time.sleep(max(args.sleep_ms, 0) / 1000.0)

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # Write JSON
    payload = {
        "generated_at": generated_at,
        "total": len(results),
        "reachable": sum(1 for r in results if r.ok),
        "unreachable": sum(1 for r in results if not r.ok),
        "results": [asdict(r) for r in results],
    }
    with open(args.out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    # Write MD
    md = render_report_md(results, generated_at)
    with open(args.out_md, "w", encoding="utf-8") as f:
        f.write(md)

    down = [r for r in results if not r.ok]
    if args.fail_on_down and down:
        print(f"ERROR: {len(down)} blocklist URL(s) unreachable.", file=sys.stderr)
        return 2

    print(f"OK: {len(results)} URLs checked; {len(down)} unreachable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
