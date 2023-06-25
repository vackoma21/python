import socket
import threading
import logging

server = socket.gethostbyname(socket.gethostname())

host = socket.gethostbyname(socket.gethostname())
port = 2207
clients = []    # Saving connections for later purpose

# LOGGING
FORMAT = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(
    filemode="a",
    filename="export.log",
    format=FORMAT,
    level=logging.INFO
)

logger = logging.getLogger(__name__)
handler = logging.FileHandler("test.log")
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


# Sends received message to one specified client/connection
def send_to_client(conn, message):
    conn[1].sendall(message.encode('ascii'))


# Loops through clients/connections and calls send_to_client function
def send_toClients_fun(conn, message):
    for client in clients:
        send_to_client(client, message)


# When server receives a message, call send_toClients_fun
# to send it to all clients/connections
def recv_message(conn, username):
    try:
        while True:
            msg = conn.recv(1024).decode('ascii')
            if msg != '':
                sentMsg = "[" + username + "]: " + msg
                logger.info(sentMsg)
                send_toClients_fun(conn, sentMsg)
            else:
                logger.warning(f'Sent message is empty, from client [{conn}]: ,{username}\'')
    except:     # Client/connection was lost
        # delete the client/connection from clients list
        for index, client in enumerate(clients):
            if conn in client:
                del clients[index]
                logger.info(f"[SERVER] Deleted {index}, {client}")
                sentMsg = f"[SERVER] {username} logged out"
                logger.info(sentMsg)
                # Send the info about user logging out to the rest of clients
                send_toClients_fun(conn, sentMsg)


# Handles new clients/connections
# First sent message is always the username
def client_fun(conn, addr):

    while True:
        msg = conn.recv(1024).decode('ascii')
        if msg != '':
            # Add username and connection to the clients list
            clients.append((msg, conn))
            newConnMsg = f"[SERVER] {msg} has been connected."
            logger.info(newConnMsg)
            # Send info about the new connection to other clients/connections
            send_toClients_fun(conn, newConnMsg)
            break
        else:
            logger.info('[SERVER] Sent message is empty')
    # Start a news thread for the new client/connection
    threading.Thread(target=recv_message, args=(conn, msg,)).start()


# Main function
# starts the server
# creates a thread for listening for new connections
def serverCode():

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        serversocket.bind((host, port))

        #print(f'Running on: {host} {port}')
        logger.info(f'[SERVER] Running on: {host} {port}')
    except Exception as e:
        logger.error(e, exc_info=True)

    serversocket.listen()

    # Keeps on listening for new connections
    while True:

        clientsocket, addr = serversocket.accept()
        logger.info(f'[SERVER] New connection: {addr[0]} {addr[1]}')
        threading.Thread(target=client_fun, args=(clientsocket, addr,)).start()


serverCode()
