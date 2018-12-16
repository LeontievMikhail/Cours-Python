import socket
from datetime import datetime


with socket.create_connection(("127.0.0.1", 10001),5) as sock:
    sock.settimeout(2)
    try:
        text=""
        text= str(datetime.now())+" hello"
        sock.sendall(text.encode("utf8"))
    except socket.timeout:
        print("send data timeout")
    except socket.error as ex:
        print("send data error:", ex)

print(datetime.now())

