import threading
import tkinter as tk
import socket

server = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
host = socket.gethostbyname(socket.gethostname())
port = 2207


# Inserts message to the chat
def insert_message(msg):
    # message to be inserted into the chat Text widget
    insertMsg = msg + "\n"

    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, insertMsg)
    chat.config(state=tk.DISABLED)


# Sends the username from username_input
# to the server and disables username_input and sendUsername
# changes the textLine state to NORMAL
def send_to_server(conn):
    username = username_input.get()
    # checks for empty username_input
    if username != '':
        conn.sendall(username.encode())
        print(f'User sent their username {username}')
        username_input.config(state=tk.DISABLED)
        sendUsername.config(state=tk.DISABLED)
        textLine.config(state=tk.NORMAL)
        textLine.delete("1.0", tk.END)
    else:   # No username was given
        print('Username cannot be empty')
    threading.Thread(target=get_message, args=(conn, )).start()


# Takes textLine content and sends it to the server on key press
def send_message(e):
    message = textLine.get("1.0", tk.END)
    textLine.delete("1.0", tk.END)
    message = message.strip('\n')
    s.sendall(message.encode('ascii'))


# Receives messages from the server
# and inserts them to the chat widget
def get_message(conn):
    while True:
        msg = conn.recv(1024).decode('ascii')
        if msg != '':
            insert_message(msg)


# Main function
# connects client to the server
# calls function to send username to the server
def clientCode():

    try:
        s.connect((host, port))
        message = "[SERVER] Connection was successful"
        insert_message(message)
    except:
        print(f'Unable to access the server {host} {port}')
    send_to_server(s)


# Tkinter
root = tk.Tk()
root.title("Chat")
root.geometry("800x500")

# main window grid config
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

# Frame config
usernameFrame.rowconfigure(0, weight=1)
usernameFrame.columnconfigure(0, weight=1)
usernameFrame.columnconfigure(1, weight=1)
usernameFrame.columnconfigure(2, weight=1)

# Creates widgets
username_input = tk.Entry(usernameFrame)
usernameLabel = tk.Label(usernameFrame, text="Username: ", font=21)
sendUsername = tk.Button(usernameFrame, text="join", font=21, command=clientCode)
chat = tk.Text(chatFrame, fg="green", borderwidth=1)
textLine = tk.Text(chatFrame, height=1, width=50, fg="green", borderwidth=1)

# Places widgets on a grid
chat.grid(row=1, column=0, columnspan=3)
textLine.grid(row=2, column=0, columnspan=3, sticky="we")
username_input.grid(row=0, column=1, sticky="we", padx=10)
usernameLabel.grid(row=0, column=0, sticky="ew")
sendUsername.grid(row=0, column=2, sticky="ew")

textLine.insert("1.0", "You can post in chat ONLY after you join with a valid username.")
textLine.config(state=tk.DISABLED)

# Messages are sent by pressing enter key
textLine.bind('<Return>', send_message)


root.mainloop()
