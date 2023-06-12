from tkinter import *



def SendText(event):
    text = textLine.get("1.0", END)
    print(text)
    textLine.delete("1.0", END)
    chat.config(state=NORMAL)
    username = "username"
    # username>> zprava\n
    msg = username + ">> " + text.strip('\n') + "\n"
    chat.insert(INSERT, username + ">> " + text.strip('\n') + "\n")
    message(text)
    chat.config(state=DISABLED)


root = Tk()
root.title("Chat")
root.geometry("400x500")


root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# frames
chatFrame = Frame(root, width=800, height=500)

chatFrame.grid(row=0, column=0, padx=10, pady=5)

#chatScroll.config(command=chat.yview)

#chatScroll = Scrollbar(root, orient="vertical")
chat = Text(chatFrame, width=50, fg="green", borderwidth=1,)
chat.config(state=DISABLED)
textLine = Text(chatFrame, height=1, width=50, fg="green", borderwidth=1)
textLine.bind('<Return>', SendText)


chat.grid(row=0, column=0)
textLine.grid(row=1, column=0)
#chatScroll.grid(row=0, column=1, columnspan=1, sticky="nsew")


root.mainloop()
