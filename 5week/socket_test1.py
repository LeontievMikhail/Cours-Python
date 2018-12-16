import socket

with socket.socket() as sock:
    sock.bind(("127.0.0.1", 10009))

    sock.listen()
    while True:
        conn, addr = sock.accept()
        with conn:
            while True:
                data=sock.recv(1024)
                if not data:
                    break
                print(data.decode("utf8"))
