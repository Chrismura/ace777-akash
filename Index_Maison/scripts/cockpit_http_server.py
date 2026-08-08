#!/usr/bin/env python3
"""HTTP local Index_Maison :17800 — sert le cockpit. Daemon léger.

Anti-cache : pywebview / Brave --app gardent sinon une vieille index.html
(alors que le navigateur avec ?v= voit la version neuve).
"""
from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler
from pathlib import Path
from socketserver import ThreadingTCPServer

INDEX = Path("/Users/christophe/ace777-test-day1/Index_Maison")
PORT = 17800


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def end_headers(self):
        # Cockpit + feed : jamais de cache disque WebKit/Chromium
        path = (self.path or "").split("?", 1)[0].lower()
        if path.endswith(
            (".html", ".js", ".json", ".css", ".svg", ".md")
        ) or path.endswith("/mission") or "/cockpit/" in path:
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
        super().end_headers()


def main() -> int:
    ThreadingTCPServer.allow_reuse_address = True
    httpd = ThreadingTCPServer(("127.0.0.1", PORT), partial(Quiet, directory=str(INDEX)))
    print(f"COCKPIT_HTTP http://127.0.0.1:{PORT}/cockpit/index.html", flush=True)
    httpd.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
