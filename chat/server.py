import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205
clients = set()
header = 64

serversocket.bind((host, port))
print(serversocket.getsockname())

while True:
    serversocket.listen()
    clientsocket, addr = serversocket.accept()
    print(clientsocket.getpeername())
    clients.add(clientsocket.getpeername())
    msg_len = clientsocket.recv(header).decode('ASCII')
    if msg_len:
        msg = clientsocket.recv(int(msg_len)).decode('ASCII')
        print(msg)
        clientsocket.sendall(b'msg')
    # clientsocket.sendall(b'Hello world!')
    clientsocket.close()
