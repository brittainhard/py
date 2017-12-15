"""
Basically, the `with` function. With open, etc. Not yield.

This is done by adding the `__enter__` and `__exit__` protocols.

I need to play around with socket more. I honestly don't know what a socket does
or how to use it. Python as a basis for learning more complex systems related
tasks. The thing.

Keep your eyes.
"""

# TODO: You need to look more deepy into how sockets work to really understand
# this one. That, and why it is sending bytes to the socket instead of the
# strings themselves.
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:

    def __init__(self, address, family=AF_INET, kind=SOCK_STREAM):
        self.address = address
        self.family = family
        self.kind = kind
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("already connected.")
        self.sock = socket(self.family, self.kind)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


conn = LazyConnection(("www.python.org", 80))


with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html/ HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))


class LazyConnection2:
    """
    This is a connection factotry. It also lets you nest multiple connections so
    you can... do something. Nest a with within a with, if thats what you kind
    of want. So it doesn't matter at what level you are working in, it will
    always exit.
    """

    def __init__(self, address, family=AF_INET, kind=SOCK_STREAM):
        self.address = address
        self.family = family
        self.kind = kind
        self.sock = None
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.kind)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self. exc_ty, exc_val, tb):
        self.connections.pop().close()
