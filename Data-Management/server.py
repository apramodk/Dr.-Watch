import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind("localhost", 80)

server.listen()

while True:
    client, addr = server.accept()
    client.add("Hello World".encode())
    print(client.recv(1024).decode())
    client.close()