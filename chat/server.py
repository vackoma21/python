import socket
import threading
import logging

server = socket.gethostbyname(socket.gethostname())

#host = '127.0.0.1'
host = socket.gethostname()
port = 2206
clients = []




def send_to_client(conn, message):
    conn[1].sendall(message.encode())
    print(f'New message was recieved from [{conn[0]}]: {message}')


def send_toClients_fun(conn, message):
    for client in clients:
        send_to_client(client, message)
        # try:
        #     client[1].sendall(message.encode('ascii'))
        # except:
        #     print(f'Message ,{message}\' could not be sent')


def recv_message(conn, username):
    while True:
        msg = conn.recv(1024).decode('ascii')
        if msg != '':
            sentMsg = "[" + username + "]: " + msg
            send_toClients_fun(conn, sentMsg)
        else:
            print(f'Sent message is empty, from client [{conn}]: ,{username}\'')


def client_fun(conn, addr):

    while True:
        msg = conn.recv(1024).decode('ascii')
        if msg != '':
            clients.append((msg, conn))
            newConnMsg = f"[SERVER]: {msg} has been connected."
            send_toClients_fun(conn, newConnMsg)
            print(f'Message was received: {msg}')
            break
        else:
            print('Sent message is empty')

    threading.Thread(target=recv_message, args=(conn, msg,)).start()


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
def serverCode():

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        serversocket.bind((host, port))

        print(f'Running on: {host} {port}')
    except:
        print('Error')

    serversocket.listen()

    while True:

        clientsocket, addr = serversocket.accept()
        print(f'New connection: {addr[0]} {addr[1]}')
        #clients.append(clientsocket.getpeername())
        threading.Thread(target=client_fun, args=(clientsocket, addr,)).start()


serverCode()
