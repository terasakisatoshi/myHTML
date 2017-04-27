import http.server

addr = "127.0.0.1"
port = 12345
server_address = (addr, port)

handler_class = http.server.SimpleHTTPRequestHandler
simple_server = http.server.HTTPServer(server_address, handler_class)
simple_server.serve_forever()
