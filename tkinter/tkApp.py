from tkinter import *

root = Tk()


def Clicked():
    label_click = Label(root, text=textThx.get(), fg="red", bg="#dee")
    label_click.grid(row=2, column=1)


textThx = StringVar()
welcomeLabel = Label(root, text="Welcome!", pady=10)
goodbyeLabel = Label(root, text="Goodbye.", pady=10)
dataE = Entry(root,textvariable=textThx)
bttnCongrats = Button(root, text="CLICK", command=Clicked, padx=20)

welcomeLabel.grid(row=0, column=0)
goodbyeLabel.grid(row=0, column=2)
bttnCongrats.grid(row=1, column=1)
dataE.grid(row=3, column=0)

root.mainloop()

