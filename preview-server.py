"""Local preview that always reloads the latest saved website files."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()


if __name__ == "__main__":
    directory = Path(__file__).resolve().parent
    handler = partial(PreviewHandler, directory=str(directory))
    server = ThreadingHTTPServer(("127.0.0.1", 8765), handler)
    print("Preview: http://127.0.0.1:8765/", flush=True)
    server.serve_forever()
