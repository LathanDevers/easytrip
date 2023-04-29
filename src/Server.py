import http.server
import cgi

class Server(http.server.BaseHTTPRequestHandler):
    def __init__(self,paths,*args,**kwargs):
        self.paths=paths
        super().__init__(*args, **kwargs)
    
    def set_headers(self,contenttype='text/html'):
        self.send_response(200)
        self.send_header('Content-type',contenttype)
        self.end_headers()
        
    def do_GET(self):
        message=""
        print(self.command)
        if self.path=="/":
            self.set_headers()
            message = open("html/index.html","r").read()
        else:
            if self.path[1:] in self.paths.keys():
                self.set_headers(contenttype=f'text/{self.paths.get(self.path[1:])}')
                message = open(self.paths.get(self.path[1:])+self.path,"r").read()
            else:
                self.send_error(404)
                #self.send_response(404)
                #self.send_header('Content-type','text/html')
                #self.end_headers()
                #message=open("html/404.html","r").read()
        self.wfile.write(bytes(message, "utf8"))
        return
    
    def do_POST(self):
        print(self.rfile.read())
        """form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })"""
        return
