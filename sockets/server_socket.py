import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 15000))
server.listen(1)
while True:
    client, address = server.accept()
    client.send(b"Potato")
    client.close()
