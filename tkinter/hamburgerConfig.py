import tkinter as tk
from tkinter import ttk
import math
from PIL import ImageTk, Image


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
            "time": tk.StringVar()
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

        # defining buttons
        self.Bttn = tk.Button(self, text="finish", command=lambda: [get_values_fce(), controller.show_frame(BurgerImage)], width=8)
        self.clearWidgets = tk.Button(self, text='clear', command=lambda: clear_inputs_fce(), fg='red', width=8, bg='#FDD')

        # placing bttn on the grid
        self.clearWidgets.grid(row=11, column=4, padx=30, pady=10)
        self.Bttn.grid(row=12, column=4, padx=30, pady=10)

        # Meat options preset
        meat_options = ['none', 'chicken', 'beef', 'pork', 'duck', 'soy']
        meat_default = tk.StringVar(self)
        meat_default.set(meat_options[0])

        # Bun options preset
        bun_options = ['plain', 'sesame seed', 'pretzel', 'potato bun', 'brioche']
        bun_default = tk.StringVar(self)
        bun_default.set(bun_options[0])

        # Sauce options preset
        sauce_options = ['none', 'ketchup', 'mustard', 'thousand island', 'chili', 'cheese', 'barbecue']
        sauce_default = tk.StringVar(self)
        sauce_default.set(sauce_options[0])

        # Cooking time preset
        meatStyle_options = ['well cooked', 'health risk']
        meatStyle_default = tk.StringVar(self)
        meatStyle_default.set(meatStyle_options[0])

        # list of all vegetables
        vegetable = ['tomato', 'cucumber', 'lettuce', 'spinach', 'onion', 'pepper', 'corn', 'mushroom', 'kale']

        # defining labels
        burgerNameLabel = tk.Label(self, text="Create a name for your very own burger: ")
        ingredients = tk.Label(self, text="Choose your ingredients: ", justify="left", anchor="w")
        meatLabel = tk.Label(self, text="Meat: ")
        meatStyleLabel = tk.Label(self, text="Cooking time: ")
        bunLabel = tk.Label(self, text="Bun: ")
        vegetablesLabel = tk.Label(self, text="Vegetables: ")
        saucesLabel = tk.Label(self, text="Sauces: ")

        burgerName = tk.Entry(self)
        meat = tk.OptionMenu(self, meat_default, *meat_options)
        bun = tk.OptionMenu(self, bun_default, *bun_options)
        sauce = tk.OptionMenu(self, sauce_default, *sauce_options)
        meatStyle = tk.OptionMenu(self, meatStyle_default, *meatStyle_options)

        burgerNameLabel.grid(row=0, column=0)
        burgerName.grid(row=0, column=1)

        ingredients.grid(row=1, column=0, sticky="w")

        # burger name

        ingredients.grid(row=2, column=0, sticky="w")

        # meat
        meatLabel.grid(row=3, column=0, sticky="w")
        meat.grid(row=3, column=1, sticky="w")

        # meat style
        meatStyleLabel.grid(row=3, column=2, sticky='w')
        meatStyle.grid(row=3, column=3, sticky='w')

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

        # collects all widgets values
        def get_values_fce():
            chosen_vegetables = []
            for index in veg:
                if veg[index].get() == 1:
                    chosen_vegetables.append(vegetable[index])

            self.controller.data['name'] = burgerName
            self.controller.data['vegetable'] = chosen_vegetables
            self.controller.data['bun'] = bun_default.get()
            self.controller.data['meat'] = meat_default.get()
            self.controller.data['sauce'] = sauce_default.get()
            self.controller.data['time'] = meatStyle_default.get()

        # clears all widget inputs
        def clear_inputs_fce():
            # restore the previous values
            bun_default.set(bun_options[0])
            meat_default.set(meat_options[0])
            sauce_default.set(sauce_options[0])
            meatStyle_default.set(meatStyle_options[0])
            burgerName.delete(0, 'end')
            for s in veg:
                veg[s].set(0)


class BurgerImage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # list for label variables for later deletion
        burgerWidgets = []

        # delete all hamburger widgets
        def clear_widgets(burger_widgets):
            if len(burger_widgets) != 0:
                for widget in burger_widgets:
                    widget.destroy()
                burger_widgets = []

        def widgets_fun(burger_widgets):

            name = self.controller.data['name'].get()
            sauce = self.controller.data['sauce']
            meat = self.controller.data['meat']
            bun = self.controller.data['bun']
            cooking_time = self.controller.data['time']
            vegetables = self.controller.data['vegetable']

            # find the correct path to selected meat with its cooking time
            # soy meat has only one cooking time
            # if no meat was selected, don't get any path
            if cooking_time == 'well cooked' and (meat != 'soy' and meat != 'none'):
                meatPNG = Image.open("hamburger/meat/" + meat + "_cooked.png")
            elif meat != 'soy' and meat != 'none':
                meatPNG = Image.open("hamburger/meat/" + meat + "_uncooked.png")
            elif meat == 'soy':
                meatPNG = Image.open("hamburger/meat/" + meat + ".png")
            else:
                meatPNG = None

            # displays the selected bun top picture
            bun_topPNG = Image.open("hamburger/bun/" + bun + "_top.png")
            bun_topPNG = bun_topPNG.resize((300, 50))
            bun_topImg = ImageTk.PhotoImage(bun_topPNG)
            bunTopL = tk.Label(self, image=bun_topImg)

            bunTopL.image = bun_topImg

            bun_bottomPNG = Image.open("hamburger/bun/" + bun + "_bottom.png")
            bun_bottomPNG = bun_bottomPNG.resize((300, 40))
            bun_bottomImg = ImageTk.PhotoImage(bun_bottomPNG)
            bun_bottomL = tk.Label(self, image=bun_bottomImg)
            bun_bottomL.image = bun_bottomImg

            burgerName = tk.Label(self, text=name)
            burgerName.grid(row=14, column=0)
            burger_widgets.append(burgerName)
            bunTopL.grid(row=15, column=0)
            burger_widgets.append(bunTopL)

            i = 1
            row = 16
            # if user selected any vegetable, create img label for each of them
            if len(vegetables) != 0:

                i = 1
                for veggie in vegetables:
                    row = 15+i

                    veggiePNG = Image.open("hamburger/veggies/" + veggie + ".png")
                    veggiePNG = veggiePNG.resize((300, 30))
                    veggieImg = ImageTk.PhotoImage(veggiePNG)
                    veggieL = tk.Label(self, image=veggieImg)
                    veggieL.image = veggieImg

                    veggieL.grid(row=row, column=0)
                    burger_widgets.append(veggieL)
                    i = i + 1

            # display corresponding meat picture
            # if any was chosen
            if meatPNG:
                meatPNG = meatPNG.resize((300, 50), Image.LANCZOS)
                meatImg = ImageTk.PhotoImage(meatPNG)
                meatL = tk.Label(self, image=meatImg)
                meatL.image = meatImg
                meatL.grid(row=row+1, column=0)
                burger_widgets.append(meatL)

            # display the chosen sauce
            if sauce != 'none':
                saucePNG = Image.open("hamburger/sauce/" + sauce + ".png")
                saucePNG = saucePNG.resize((300, 25), Image.LANCZOS)
                sauceImg = ImageTk.PhotoImage(saucePNG)
                sauceL = tk.Label(self, image=sauceImg)
                sauceL.image = sauceImg
                sauceL.grid(row=16 + i, column=0)
                burger_widgets.append(sauceL)

            # displays the selected bun bottom picture
            bun_bottomL.grid(row=17+i, column=0)
            burger_widgets.append(bun_bottomL)

        self.nameLa = tk.Label(self, text='LABEL')
        self.Label = tk.Label(self, text="BurgerImage")
        self.Bttn = tk.Button(self, text="back", command=lambda: [controller.show_frame(MainWindow), clear_widgets(burgerWidgets)])
        self.Label.grid(row=11, column=4, padx=10, pady=10)
        self.Bttn.grid(row=12, column=4, padx=10, pady=10)

        self.showBttn = tk.Button(self, text='show', command=lambda: [widgets_fun(burgerWidgets)])
        self.showBttn.grid(row=50, column=4)


app = Windows()
app.mainloop()

