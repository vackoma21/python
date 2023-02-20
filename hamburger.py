import tkinter


class MainWindow(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.ingredients = None
        self.vegetable1 = None
        self.vegetable2 = None
        self.vegetable3 = None
        self.vegetable4 = None
        self.vegetable5 = None
        self.vegetable6 = None
        self.vegetable7 = None
        self.vegetable8 = None
        self.vegetable9 = None

        self.meat = None
        self.bun = None
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
        meatOptions = ['chicken', 'beef', 'pork', 'duck', 'soy']
        meatDefault = tkinter.StringVar(root)
        meatDefault.set("none")

        bunOptions = ['plain', 'sesame seed', 'pretzel', 'potato bun', 'brioche']
        bunDefault = tkinter.StringVar(root)
        bunDefault.set(bunOptions[0])

        vegetable = ['tomato', 'cucumber', 'lettuce', 'spinach', 'onion', 'pepper', 'corn', 'mushrooms', 'kale']
        fruit = ['pineapple', 'mango', 'apple', 'peach', 'pear', 'avocado']

        self.burgerNameLabel = tkinter.Label(text="Create a name for your very own burger")
        self.ingredients = tkinter.Label(text="Choose your ingredients: ")
        self.meatLabel = tkinter.Label(text="Meat: ")
        self.meatStyleLabel = tkinter.Label(text="Cooking time: ")
        self.bunLabel = tkinter.Label(text="Bun: ")
        self.vegetablesLabel = tkinter.Label(text="Vegetables: ")
        self.saucesLabel = tkinter.Label(text="Sauces: ")

        self.burgerName = tkinter.Entry()

        self.meat = tkinter.OptionMenu(root, meatDefault, *meatOptions)
        self.bun = tkinter.OptionMenu(root, bunDefault, *bunOptions)
        self.vegetable1 = tkinter.Checkbutton(root, text=vegetable[0])
        self.vegetable2 = tkinter.Checkbutton(root, text=vegetable[1])
        self.vegetable3 = tkinter.Checkbutton(root, text=vegetable[2])
        self.vegetable4 = tkinter.Checkbutton(root, text=vegetable[3])
        self.vegetable5 = tkinter.Checkbutton(root, text=vegetable[4])
        self.vegetable6 = tkinter.Checkbutton(root, text=vegetable[5])
        self.vegetable7 = tkinter.Checkbutton(root, text=vegetable[6])
        self.vegetable8 = tkinter.Checkbutton(root, text=vegetable[7])
        self.vegetable9 = tkinter.Checkbutton(root, text=vegetable[8])

        # display form

        # burger name
        self.burgerNameLabel.pack()
        self.burgerName.pack()

        self.ingredients.pack()

        # meat
        self.meatLabel.pack()
        self.meat.pack()

        # bun
        self.bunLabel.pack()
        self.bun.pack()

        # vegetables
        self.vegetablesLabel.pack()
        self.vegetable1.pack()
        self.vegetable2.pack()
        self.vegetable3.pack()
        self.vegetable4.pack()
        self.vegetable5.pack()
        self.vegetable6.pack()
        self.vegetable7.pack()
        self.vegetable8.pack()
        self.vegetable9.pack()


root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()
