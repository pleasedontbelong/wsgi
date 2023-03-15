from datetime import datetime
import logging

logger = logging.getLogger(__name__)
logger.debug("App imported")


def application(environ: dict, start_response: callable):
    response_body = f"""
        <h1>Hello world</h1>
        <p>It's {datetime.now()} requests</p>
        <p>{environ}</p>
    """
    status = "200 OK"

    response_headers = [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response_body))),
    ]

    start_response(status, response_headers)
    return [str.encode(response_body)]


# call_count = 0


# def application(environ: dict, start_response: callable):
#     global call_count
#     response_body = f"""
#         <h1>Hello world</h1>
#         <p>Served {call_count} requests</p>
#     """
#     call_count += 1
#     status = "200 OK"

#     response_headers = [
#         ("Content-Type", "text/html"),
#         ("Content-Length", str(len(response_body))),
#     ]

#     start_response(status, response_headers)
#     return [str.encode(response_body)]


# def application(environ: dict, start_response: callable):
#     logger.debug("App started")
#     status = "200 OK"

#     response_headers = [
#         ("Content-Type", "text/html"),
#     ]

#     start_response(status, response_headers)
#     yield b"wait!<br/>"
#     yield b"wait!<br/>"
#     while True:
#         message = input("write something:")
#         yield str.encode(message + "<br/>")
