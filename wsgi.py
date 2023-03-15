from wsgiref.simple_server import make_server
from app import application


if __name__ == "__main__":
    # single call then exit
    # httpd = make_server("localhost", 8000, application)
    # httpd.handle_request()

    # we could make it handle all requests
    with make_server("", 8000, application) as httpd:
        print("Listening on port 8000....")
        httpd.serve_forever()

    httpd = make_server("localhost", 8000, application)
    while True:
        httpd.handle_request()
