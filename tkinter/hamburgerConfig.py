import tkinter as tk
from tkinter import ttk
import math

# window class that holds all the frames
class Windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Hamburger Config")
        
        # defines a dict of values shared within the whole app
        self.data = {
            "name": tk.StringVar(),
            "vegetables": [],
            "meat": tk.StringVar(),
            "bun": tk.StringVar(),
            "sauce": tk.StringVar(),
        }
        
        # creates the main frame in which other frames reside
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # dictionary of all frames (excluding the Windows one)
        self.frames = {}

        for F in (MainWindow, BurgerImage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # calls function that tkraise the next frame on top
        self.show_frame(MainWindow)
    
    # function that puts inputted frame on top
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        # print('hi')

    def update_config(self):
        self.data['name'].get()


# class with user inputs about the custom hamburger
class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Label = ttk.Label(self, text="MainWindow")
        self.Bttn = ttk.Button(self, text="img", command=lambda: [get_values_fce(), controller.show_frame(BurgerImage)])

        self.Label.grid(row=11, column=4, padx=10, pady=10)
        self.Bttn.grid(row=12, column=4, padx=10, pady=10)

        # self.burgerNameLabel1 = ttk.Label(self, text="Create a name for your very own burger")
        # self.burgerNameLabel1.grid(row=2, column=4, padx=10, pady=10)

        meat_options = ['none', 'chicken', 'beef', 'pork', 'duck', 'soy']
        meat_default = tk.StringVar(self)
        meat_default.set(meat_options[0])

        bun_options = ['plain', 'sesame seed', 'pretzel', 'potato bun', 'brioche']
        bun_default = tk.StringVar(self)
        bun_default.set(bun_options[0])

        sauce_options = ['none', 'ketchup', 'mustard', 'thousand island', 'chili', 'cheese', 'barbecue']
        sauce_default = tk.StringVar(self)
        sauce_default.set(sauce_options[0])

        vegetable = ['tomato', 'cucumber', 'lettuce', 'spinach', 'onion', 'pepper', 'corn', 'mushrooms', 'kale']

        burgerNameLabel = ttk.Label(self, text="Create a name for your very own burger: ")
        ingredients = ttk.Label(self, text="Choose your ingredients: ", justify="left", anchor="w")
        meatLabel = ttk.Label(self, text="Meat: ")
        meatStyleLabel = ttk.Label(self, text="Cooking time: ")
        bunLabel = ttk.Label(self, text="Bun: ")
        vegetablesLabel = tk.Label(self, text="Vegetables: ")
        saucesLabel = ttk.Label(self, text="Sauces: ")

        self.burgerName = ttk.Entry(self)
        meat = ttk.OptionMenu(self, meat_default, *meat_options)
        bun = ttk.OptionMenu(self, bun_default, *bun_options)
        sauce = ttk.OptionMenu(self, sauce_default, *sauce_options)

        burgerNameLabel.grid(row=0, column=0)
        self.burgerName.grid(row=0, column=1)

        ingredients.grid(row=1, column=0, sticky="w")

        # burger name

        ingredients.grid(row=2, column=0, sticky="w")

        # meat
        meatLabel.grid(row=3, column=0, sticky="w")
        meat.grid(row=3, column=1, sticky="w")

        # bun
        bunLabel.grid(row=4, column=0, sticky="w")
        bun.grid(row=4, column=1, sticky="w")

        # sauces

        saucesLabel.grid(row=5, column=0, sticky="w")
        sauce.grid(row=5, column=1, sticky="w")

        # vegetables
        vegetablesLabel.grid(row=6, column=0, sticky="w")
       
        # appends only checked boxes
        def append_vegetable_fce():
            chosen_vegetables = []
            for index in veg:
                if veg[index].get() == 1:
                    chosen_vegetables.append(vegetable[index])
            print(chosen_vegetables)
            return chosen_vegetables
        # dict with the final values 
        veg = {}
        col = 2
        # loop that creates vegetable checkboxes
        for x in range(len(vegetable)):
            if col == 1:
                col = 2
            else:
                col = col - 1
            row = math.ceil(x / 2)
            if row == 0:
                row = 1
            if x >= 2:
                row = row + 1

            veg[x] = tk.IntVar(value=0)
            vegetable_box = tk.Checkbutton(
                self, text=vegetable[x], variable=veg[x],
                command=lambda o=append_vegetable_fce: append_vegetable_fce,
                borderwidth=5, border=2
            )
            vegetable_box.grid(row=5 + row, column=col, sticky="w")
            # print(5+row)

        def get_values_fce():
            # print("Burger name")
            # print(burgerName.get())
            # print("Vegetable")
            # for i in range(len(chosen_vegetables)):
            #     print(chosen_vegetables[i])
            # print("Meat")
            # print(meat_default.get())
            # print("Sauce")
            # print(sauce_default.get())
            # print("Bun")
            # print(bun_default.get())
            # print()
            chosen_vegetables = []
            for index in veg:
                if veg[index].get() == 1:
                    chosen_vegetables.append(vegetable[index])

            self.controller.data['name'] = self.burgerName
            self.controller.data['vegetable'] = chosen_vegetables
            self.controller.data['bun'] = bun_default.get()
            self.controller.data['meat'] = meat_default.get()
            self.controller.data['sauce'] = sauce_default.get()

            global nameLa
            # nameL = BurgerImage(parent, controller)
            main_window = app
            text = BurgerImage(parent, controller).nameLa
            text["text"] = self.controller.data['name']

            # return self.name, self.veggies, bunV, meatV, sauceV

        def clear_inputs_fce():
            chosen_vegetables = []
            for index in veg:
                if veg[index].get() == 1:
                    chosen_vegetables.append(vegetable[index])

            # save values about the hamburger
            self.name = self.controller.data['name'].get()
            self.veggies = chosen_vegetables
            self.bunV = bun_default.get()
            self.meatV = meat_default.get()
            self.sauceV = sauce_default.get()

            # restore the previous values
            bun_default.set(bun_options[0])
            meat_default.set(meat_options[0])
            sauce_default.set(sauce_options[0])

            print(self.name)
            print(self.veggies)
            print(self.bunV)
            print(self.meatV)
            print(self.sauceV)


class BurgerImage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.nameLa = tk.Label(self, text='LABEL')
        self.Label = ttk.Label(self, text="BurgerImage")
        self.Bttn = ttk.Button(self, text="mw", command=lambda: [controller.show_frame(MainWindow), print(self.controller.data['name'].get())])
        self.Label.grid(row=11, column=4, padx=10, pady=10)
        self.Bttn.grid(row=12, column=4, padx=10, pady=10)
        # name = self.controller.data['name'].get()
        # self.nameLa = tk.Label(self, textvariable=name)
        #
        # self.nameLa.grid(row=0, column=0)
        self.widgets()

    def widgets(self):
        global nameLa
        # self.name = self.controller.data['name'].get()
        self.nameLa = tk.Label(self, text='LABEL')
        # self.nameLa["text"] = 'HU'

        self.nameLa.grid(row=0, column=0)


app = Windows()
app.mainloop()

