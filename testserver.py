import SimpleHTTPServer
import SocketServer

PORT = 80

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    pass

Handler.extensions_map['.shtml'] = 'text/html'
Handler.extensions_map[''] = 'text/plain'
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
