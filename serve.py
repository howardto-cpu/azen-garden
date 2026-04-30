"""
Azen Garden dev server — run with: python serve.py
Serves the project at http://localhost:3000
"""
import http.server
import socketserver
import os

PORT = 3000

MIME = {
    ".html":  "text/html; charset=utf-8",
    ".css":   "text/css",
    ".js":    "application/javascript",
    ".mjs":   "application/javascript",
    ".jpg":   "image/jpeg",
    ".jpeg":  "image/jpeg",
    ".png":   "image/png",
    ".gif":   "image/gif",
    ".svg":   "image/svg+xml",
    ".webp":  "image/webp",
    ".mp4":   "video/mp4",
    ".woff":  "font/woff",
    ".woff2": "font/woff2",
    ".ico":   "image/x-icon",
}

class Handler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        ext = os.path.splitext(path)[1].lower()
        return MIME.get(ext, "application/octet-stream")

    def log_message(self, format, *args):
        print(f"  {args[0]} {args[1]}")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"\n  Azen Garden dev server running at http://localhost:{PORT}\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
