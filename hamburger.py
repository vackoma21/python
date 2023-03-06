import tkinter as tk
import math

# class BurgerWindow(tkinter.Toplevel):
#
#     def __int__(self, master=None):
#         super().__init__(master=root)
#         self.title("Hamburger!")
#         self.geometry("800x500")
#
#         self.label = tkinter.Label(self, text="Hi")
#         self.label.pack()
#


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("app")

        container = tk.Frame(self, height=600, width=400)
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
        self.vegetable_box = None
        self.create = tk.Button(text="create", command=lambda: controller.show_frame(BurgerImage))
        self.ingredients = None

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
        self.sauce = None
        self.parent = parent

        # grid configuration
        # self.parent.rowconfigure(0, weight=500)
        # self.parent.rowconfigure(1)

        # self.parent.title('A window app')
        # self.parent.geometry("800x500")

        self.create_widgets()

    def create_widgets(self):
        def doThis():
            print("Burger name")
            print(chosen_burger_name.get())
            print("Vegetable")
            for i in range(len(chosen_vegetables)):
                print(chosen_vegetables[i])
            print("Meat")
            print(meat_default.get())
            print("Sauce")
            print(sauce_default.get())
            print("Bun")
            print(bun_default.get())
            print()

        chosen_vegetables = []
        chosen_burger_name = tk.StringVar()

        meat_options = ['none', 'chicken', 'beef', 'pork', 'duck', 'soy']
        meat_default = tk.StringVar(root)
        meat_default.set(meat_options[0])

        bun_options = ['plain', 'sesame seed', 'pretzel', 'potato bun', 'brioche']
        bun_default = tk.StringVar(root)
        bun_default.set(bun_options[0])

        sauce_options = ['none', 'ketchup', 'mustard', 'thousand island', 'chili', 'cheese', 'barbecue']
        sauce_default = tk.StringVar(root)
        sauce_default.set(sauce_options[0])

        vegetable = ['tomato', 'cucumber', 'lettuce', 'spinach', 'onion', 'pepper', 'corn', 'mushrooms', 'kale']

        self.burgerNameLabel = tk.Label(text="Create a name for your very own burger")
        self.ingredients = tk.Label(text="Choose your ingredients: ")
        self.meatLabel = tk.Label(text="Meat: ")
        self.meatStyleLabel = tk.Label(text="Cooking time: ")
        self.bunLabel = tk.Label(text="Bun: ")
        self.vegetablesLabel = tk.Label(text="Vegetables: ")
        self.saucesLabel = tk.Label(text="Sauces: ")

        self.burgerName = tk.Entry(textvariable=chosen_burger_name)

        self.meat = tk.OptionMenu(root, meat_default, *meat_options)
        self.bun = tk.OptionMenu(root, bun_default, *bun_options)
        self.sauce = tk.OptionMenu(root, sauce_default, *sauce_options)

        # display form

        # burger name
        self.burgerNameLabel.grid(row=0, column=0)
        self.burgerName.grid(row=1, column=0)

        self.ingredients.grid(row=2, column=0)

        # meat
        self.meatLabel.grid(row=3, column=0)
        self.meat.grid(row=3, column=1)

        # bun
        self.bunLabel.grid(row=4, column=0)
        self.bun.grid(row=4, column=1)

        # sauces

        self.saucesLabel.grid(row=5, column=0)
        self.sauce.grid(row=5, column=1)

        # vegetables
        self.vegetablesLabel.grid(row=6, column=0)

        col = 2
        for x in range(len(vegetable)):
            print(x)
            if col == 1:
                col = 2
            else:
                col = col - 1
            row = math.ceil(x / 2)
            if row == 0:
                row = 1
            if x >= 2:
                row = row+1
            self.vegetable_box = tk.Checkbutton(root, text=vegetable[x], variable=vegetable[x], command=lambda i=vegetable[x]: chosen_vegetables.append(i), borderwidth=5, border=2)
            self.vegetable_box.grid(row=5+row, column=col)

        # bttn

        self.create.grid(row=16, column=0)


class BurgerImage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.label = tk.Label(text="Second page")


root = tk.Tk()
app = Windows()
app.mainloop()
