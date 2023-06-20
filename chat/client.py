import threading
import tkinter as tk
import socket

server = socket.gethostbyname(socket.gethostname())

host = socket.gethostname()
port = 2206
user = []

root = tk.Tk()
root.title("Chat")
root.geometry("800x500")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# frames
chatFrame = tk.Frame(root, width=800, height=250)
chatFrame.grid(row=0, column=0, padx=10, pady=5)

usernameFrame = tk.Frame(chatFrame, bg="red", width=800)
usernameFrame.grid(row=0, column=0, pady=5, sticky="nsew", columnspan=3)

#chatScroll.config(command=chat.yview)

#chatScroll = Scrollbar(root, orient="vertical")
username = tk.Entry(usernameFrame)
usernameLabel = tk.Label(usernameFrame, text="Username: ")
sendUsername = tk.Button(usernameFrame, text="login")
chat = tk.Text(chatFrame, fg="green", borderwidth=1)
textLine = tk.Text(chatFrame, height=1, width=50, fg="green", borderwidth=1)


chat.grid(row=1, column=0, columnspan=3)
textLine.grid(row=2, column=0, columnspan=3, sticky="we")
username.grid(row=0, column=1, sticky="nsew")
usernameLabel.grid(row=0, column=0, sticky="nsew")
sendUsername.grid(row=0, column=2, sticky="nsew")

def send_to_server(conn):
    username = input('Username: ')
    if username != '':
        conn.sendall(username.encode('ascii'))
        print(f'User sent their username {username}')
    else:
        print('Username cannot be empty')
        exit(0)
    threading.Thread(target=get_message, args=(conn, )).start()

    send_message(conn)


def send_message(conn):
    try:
        while True:
            message = input()
            conn.sendall(message.encode('ascii'))
    except:
        print(f'User logged out {user[0]}')


def get_message(conn):
    while True:
        msg = conn.recv(1024).decode('ascii')
        user.append(msg)
        if msg != '':
            username = msg.split(':')[0]
            content = msg.split(':')[1]
            print(msg)
        else:
            print('Message from client is empty.')


def clientCode():
    root.mainloop()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        print(f'Connected to the server')
    except:
        print(f'Unable to access the server {host} {port}')
    send_to_server(s)


#msg = s.recv(1024)
#print(msg.decode('ascii'))
#s.close()
#message = 'Hi'
#s.send(b'hi')
#s.send(message)



# def addText(sMsg):
#     text = sMsg.decode('ascii')
#     print(text)
#     chat.config(state=NORMAL)
#     username = "username"
#     # username>> zprava\n
#     msg = username + ">> " + text + "\n"
#     print(msg)
#     chat.insert(INSERT, msg)
#     chat.config(state=DISABLED)
#
#
#
# def message(text):
#     message = text.encode('ascii')
#     msg_len = len(message)
#     print(msg_len)
#     send_len = str(msg_len).encode('ascii')
#     #send_len += b' ' * (header - len(send_len))
#     #s.send(send_len)
#     s.send(message)
#
#
# def SendText(event):
#     msg = textLine.get("1.0", END)
#     print('-------------')
#     print(msg)
#     textLine.delete("1.0", END)
#     username = "username"
#     # username>> zprava\n
#     #msg = username + ">> " + text.strip('\n') + "\n"
#     #chat.insert(INSERT, username + ">> " + text.strip('\n') + "\n")
#     msg = msg.strip('\n')
#     s.send(msg)
#     #message(msg)
#
#
# root = Tk()
# root.title("Chat")
# root.geometry("400x500")
#
#
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)
#
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
#
# # frames
# chatFrame = Frame(root, width=800, height=500)
#
# chatFrame.grid(row=0, column=0, padx=10, pady=5)
#
# #chatScroll.config(command=chat.yview)
#
# #chatScroll = Scrollbar(root, orient="vertical")
# chat = Text(chatFrame, width=50, fg="green", borderwidth=1)
# chat.config(state=DISABLED)
# textLine = Text(chatFrame, height=1, width=50, fg="green", borderwidth=1)
# textLine.bind('<Return>', SendText)
#
#
# chat.grid(row=0, column=0)
# textLine.grid(row=1, column=0)
# #chatScroll.grid(row=0, column=1, columnspan=1, sticky="nsew")
#
#
# root.mainloop()

clientCode()
