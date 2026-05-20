from http.server import BaseHTTPRequestHandler, HTTPServer

# Store data in memory
stored_data = "SUPER SECRET DO NOT LEAK!!!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to GET requests with the stored plaintext data."""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(stored_data.encode("utf-8"))


# Start the server
server = HTTPServer(("", 8080), Handler)
print("Server running on port 8080...")
server.serve_forever()
