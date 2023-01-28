"""
Write a simple wsgi compatible application that prints the username, remote address, user agent,
path and your surname(see below). Add a simple middleware that adds the key SURNAME with the value of your surname
to the environ.
Add another middleware that changes the formatting of all the symbols to be lowercase
(except of the first ones in sentence and your surname). Use two middlewares simultaneously.
"""
from webob import Response
from wsgiref.simple_server import make_server

from middleware import Middleware

HOST = "localhost"
PORT = 8001


class MyApp:
    def __call__(self, environ, start_response):
        response = Response()
        response.text = self.create_response(environ)
        return response(environ, start_response)

    @staticmethod
    def create_response(environ):
        return f"User_name: {environ['USERNAME']} {environ['SURNAME']}, address: {environ['REMOTE_ADDR']}," \
               f" agent: {environ['HTTP_USER_AGENT']}"


if __name__ == "__main__":
    input_sername = input("Input your surname: ")
    with make_server(HOST, PORT, app=Middleware(MyApp(), input_sername)) as server:
        print(f"Server started at http://{HOST}:{PORT}")
        server.serve_forever()
