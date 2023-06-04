import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = socket.gethostbyname(socket.gethostname())

header = 64
host = socket.gethostname()
port = 2205

s.connect((server, port))
#msg = s.recv(1024)
#print(msg.decode('ascii'))
#s.close()
#message = 'Hi'
#s.send(b'hi')
#s.send(message)


def message(text):
    message = text.encode('ascii')
    msg_len = len(message)
    send_len = str(msg_len).encode('ascii')
    send_len += b' ' * (header - len(send_len))
    s.send(send_len)
    s.send(message)


message('HELL O')
