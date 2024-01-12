"""Dependency-free parcel API used by the interview exercise."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def response(path):
    if path in ("/healthz", "/readyz"):
        return 200, {"status": "ok"}
    if path.startswith("/shipments/"):
        try:
            data = json.loads(Path(os.getenv("DATA_FILE", "data/shipments.json")).read_text())
        except (OSError, ValueError):
            return 503, {"error": "data unavailable"}
        shipment = data.get(path.removeprefix("/shipments/"))
        return (200, shipment) if shipment else (404, {"error": "not found"})
    return 404, {"error": "not found"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, body = response(self.path)
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == "__main__":
    ThreadingHTTPServer((os.getenv("HOST", "127.0.0.1"), int(os.getenv("PORT", "8080"))), Handler).serve_forever()
