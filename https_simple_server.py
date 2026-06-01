from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

stored_data = "SUPER SECRET DO NOT LEAK!!!"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(stored_data.encode("utf-8"))

server_address = ("", 8443)
httpd = HTTPServer(server_address, Handler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("HTTPS server running on https://localhost:8443")
httpd.serve_forever()
