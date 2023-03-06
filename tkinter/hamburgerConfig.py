import tkinter as tk
import math


class Windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Hamburger Config")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (MainWindow, BurgerImage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainWindow)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Label = tk.Label(self, text="MainWindow")
        self.Bttn = tk.Button(self, text="img", command=lambda: controller.show_frame(BurgerImage))

        self.Label.pack()
        self.Bttn.pack()

        self.burgerNameLabel = tk.Label(text="Create a name for your very own burger")
        self.burgerNameLabel.pack()


class BurgerImage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Label = tk.Label(self, text="BurgerImage")
        self.Bttn = tk.Button(self, text="mw", command=lambda: controller.show_frame(MainWindow))
        self.Label.pack()
        self.Bttn.pack()


app = Windows()
app.mainloop()

