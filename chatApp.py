from tkinter import *

root = Tk()
root.title("Chat")
root.geometry("250x500")


root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

chatScroll = Scrollbar(root, orient="vertical")
chat = Text(root, width=50, yscrollcommand=chatScroll.set, fg="green")
textLine = Text(root, height=2, width=50, fg="green")

chatScroll.config(command=chat.yview)

chat.grid(row=0, column=0)
textLine.grid(row=1, column=0)
chatScroll.grid(row=0, column=1, columnspan=1, sticky="nsew")


root.mainloop()
