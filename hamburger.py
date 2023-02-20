import tkinter

class MainWindow(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.meat = None
        self.saucesLabel = None
        self.vegetablesLabel = None
        self.bunLabel = None
        self.meatStyleLabel = None
        self.meatLabel = None
        self.burgerName = None
        self.button = None
        self.burgerNameLabel = None
        self.parent = parent

        # grid configuration
        # self.parent.rowconfigure(0, weight=500)
        # self.parent.rowconfigure(1)

        self.parent.title('A window app')
        self.parent.geometry("800x500")

        self.create_widgets()

    def create_widgets(self):

        meatOptions = ['chicken', 'beef', 'pork', 'duck']

        self.burgerNameLabel = tkinter.Label(text="Create a name for your very own burger")
        self.meatLabel = tkinter.Label(text="Meat: ")
        self.meatStyleLabel = tkinter.Label(text="Cooking time: ")
        self.bunLabel = tkinter.Label(text="Bun: ")
        self.vegetablesLabel = tkinter.Label(text="Vegetables: ")
        self.saucesLabel = tkinter.Label(text="Sauces: ")

        self.burgerName = tkinter.Entry()

        self.meat = tkinter.OptionMenu(root, *meatOptions)

        # display form
        self.meat.pack()


root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()
