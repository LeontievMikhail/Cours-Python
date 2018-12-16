import socket

with socket.create_connection(("127.0.0.1", 11001)) as sock:
    sock.sendall("Hello world-".encode("utf8"))