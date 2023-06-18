import socket
from _thread import *
import threading

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2206
clients = []

serversocket.bind((host, port))
print(serversocket.getsockname())


def send_toClients_fun(conn, message):
    for client in clients:
        try:
            client[1].sendall(message.encode('ascii'))
        except:
            print(f'Message ,{message}\' could not be sent')


def recv_message(conn, username):
    while True:
        msg = conn.recv(1024).decode('ascii')
        if msg != '':
            sentMsg = "[" + username + "]: " + msg
            send_toClients_fun(conn, sentMsg)
        else:
            print(f'Sent message is empty, from client {username}')


def client_fun(conn, addr):

    while True:
        msg = conn.recv(1024).decode('ascii')
        if msg != '':
            clients.append((msg, conn))
            break
        else:
            print('Sent message is empty')

    threading.Thread(target=recv_message, args=(clientsocket, msg,)).start()


# def client_fun(conn, addr):
#     conn.send('Connected')
#     while True:
#         try:
#             msg = conn.recv(1024)
#             if msg:
#                 sender = addr[0]
#                 message = "[" + sender + "]: " + msg
#                 print(message)
#                 send_toClients_fun(conn, message)
#             else:
#                 if conn in clients:
#                     clients.remove(conn)
#         except:
#             continue

serversocket.listen()

while True:

    clientsocket, addr = serversocket.accept()
    print(f'New connection: {addr[0]} {addr[1]}')
    #clients.append(clientsocket.getpeername())
    threading.Thread(target=client_fun, args=(clientsocket, addr,)).start()
    # msg_len = clientsocket.recv(header).decode('ASCII')
    # if msg_len:
    #     msg = clientsocket.recv(int(msg_len)).decode('ASCII')
    #     print(msg)
    #     clientsocket.sendall(b'msg')
    # clientsocket.sendall(b'Hello world!')
    #start_new_thread(client_fun, (clientsocket, addr))

