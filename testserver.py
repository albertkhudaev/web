import wsgiref
from wsgiref.simple_server import make_server, demo_app
from hello import app
from ask.ask.wsgi import application


with make_server('localhost', 8000, application) as httpd:
    print("server HTTP on port 8000")
    httpd.serve_forever()