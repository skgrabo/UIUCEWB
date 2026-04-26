#!/usr/bin/env python3

from __future__ import annotations

import argparse
import http.server
import socketserver


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve this site locally.")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on (default: 8000)")
    args = parser.parse_args()

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer((args.host, args.port), handler) as httpd:
        url = f"http://{args.host}:{args.port}/"
        print(f"Serving at {url} (Ctrl+C to stop)")
        httpd.serve_forever()


if __name__ == "__main__":
    main()

