import threading
import tkinter as tk
import socket

server = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
host = socket.gethostbyname(socket.gethostname())
port = 2207
user = []


def insert_message(msg):
    # message to be inserted into the chat Text widget
    insertMsg = msg + "\n"

    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, insertMsg)
    chat.config(state=tk.DISABLED)


def send_to_server(conn):
    #username = input('Username: ')
    username = username_input.get()
    if username != '':
        conn.sendall(username.encode('ascii'))
        print(f'User sent their username {username}')
        username_input.config(state=tk.DISABLED)
        sendUsername.config(state=tk.DISABLED)
    else:
        #print('Username cannot be empty')
        pass
        #exit(0)
    threading.Thread(target=get_message, args=(conn, )).start()

    #send_message(conn)


def send_message(e):
    message = textLine.get("1.0", tk.END)
    textLine.delete("1.0", tk.END)
    message = message.strip('\n')
    s.sendall(message.encode('ascii'))
    print('TEXC')
    #insert_message(message)


def get_message(conn):
    while True:
        msg = conn.recv(1024).decode('ascii')
        user.append(msg)
        if msg != '':
            print(msg)
            insert_message(msg)
        else:
            print('Message from client is empty.')


def clientCode():

    try:
        s.connect((host, port))
        print(f'Connected to the server')
        message = "[SERVER] Connection was successful"
        insert_message(message)
    except:
        print(f'Unable to access the server {host} {port}')
    send_to_server(s)


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

usernameFrame = tk.Frame(chatFrame, width=800)
usernameFrame.grid(row=0, column=0, pady=5, sticky="we", columnspan=3)

usernameFrame.rowconfigure(0, weight=1)
usernameFrame.columnconfigure(0, weight=1)
usernameFrame.columnconfigure(1, weight=1)
usernameFrame.columnconfigure(2, weight=1)

#chatScroll.config(command=chat.yview)

#chatScroll = Scrollbar(root, orient="vertical")
username_input = tk.Entry(usernameFrame)
usernameLabel = tk.Label(usernameFrame, text="Username: ", font=21)
sendUsername = tk.Button(usernameFrame, text="join", font=21, command=clientCode)
chat = tk.Text(chatFrame, fg="green", borderwidth=1)
textLine = tk.Text(chatFrame, height=1, width=50, fg="green", borderwidth=1)


chat.grid(row=1, column=0, columnspan=3)
textLine.grid(row=2, column=0, columnspan=3, sticky="we")
username_input.grid(row=0, column=1, sticky="we", padx=10)
usernameLabel.grid(row=0, column=0, sticky="ew")
sendUsername.grid(row=0, column=2, sticky="ew")


textLine.bind('<Return>', send_message)

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

#clientCode()

root.mainloop()
