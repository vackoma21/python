import socket
import threading

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

header = 64

server = socket.gethostbyname(socket.gethostname())     # ipv4
host = socket.gethostname()
port = 2205
clients = set()
threading.Lock()

serversocket.bind((server, port))
#print(serversocket.getsockname())


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    clients.add(conn)
    while connected:
        #msg_len = conn.recv(header).decode('ascii')

        #if msg_len:
            #msg_len = int(msg_len)
        msg = conn.recv(1024).decode('ascii')
        print(f"[{addr}] {msg}")
        message = msg.encode('ASCII')
        conn.send(message)
        #serversocket.sendall(msg.encode('ascii'))

    conn.close()

def start():
    serversocket.listen()
    #print(f"[LISTENING] Server is listening on {server}")
    while True:
        conn, addr = serversocket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

        #print(clientsocket.getpeername())
        #clientsocket.sendall(b'Hello world!')
        #clientsocket.close()


#print("[STARTING] server is starting...")
start()
