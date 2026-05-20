from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

# Store data in memory
stored_data = "SUPER SECRET DO NOT LEAK!!!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to GET requests with the stored data over HTTPS."""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(stored_data.encode("utf-8"))


# Start the server
server_address = ("", 8443)  # Use port 8443 for HTTPS
httpd = HTTPServer(server_address, Handler)

# Wrap the server with SSL/TLS
# This version matches the original classroom/demo code.
# Note: ssl.wrap_socket() may show a deprecation warning in newer Python versions.
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    server_side=True,
    keyfile="server.key",      # Path to your private key
    certfile="server.crt",     # Path to your certificate
    ssl_version=ssl.PROTOCOL_TLS,
)

print("HTTPS server running on port 8443...")
httpd.serve_forever()
