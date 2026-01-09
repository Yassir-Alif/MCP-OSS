
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = "ui"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    # Change into the project root if needed, but we assume we are running from root
    if not os.path.exists(DIRECTORY):
        print(f"Error: Directory '{DIRECTORY}' not found.")
        sys.exit(1)

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving UI at http://localhost:{PORT}")
        print("Press Ctrl+C to stop.")
        # Try to open browser
        try:
            webbrowser.open(f"http://localhost:{PORT}")
        except:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server.")
