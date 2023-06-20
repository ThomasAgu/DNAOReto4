from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith('.css'):
            self.send_header('Content-Type', 'text/css')
        super().end_headers()

# Configurar el servidor
host = 'localhost'
port = 8000
server_address = (host, port)
httpd = HTTPServer(server_address, MyHTTPRequestHandler)

# Iniciar el servidor
print(f'Servidor iniciado en http://{host}:{port}')
httpd.serve_forever()