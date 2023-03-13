import tkinter as tk
import math

root = tk.Tk()

chosen_vegetables = []
chosen_burger_name = tk.StringVar(root)

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

root.title("Hamburger Config")

burgerNameLabel = tk.Label(text="Create a name for your very own burger: ")
ingredients = tk.Label(text="Choose your ingredients: ", justify="left", anchor="w")
meatLabel = tk.Label(text="Meat: ")
meatStyleLabel = tk.Label(text="Cooking time: ")
bunLabel = tk.Label(text="Bun: ")
vegetablesLabel = tk.Label(text="Vegetables: ")
saucesLabel = tk.Label(text="Sauces: ")

burgerName = tk.Entry()
meat = tk.OptionMenu(root, meat_default, *meat_options)
bun = tk.OptionMenu(root, bun_default, *bun_options)
sauce = tk.OptionMenu(root, sauce_default, *sauce_options)

create = tk.Button(text="create")

burgerNameLabel.grid(row=0, column=0)
burgerName.grid(row=0, column=1)

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
    vegetable_box = tk.Checkbutton(
        root, text=vegetable[x],
        command=lambda i=vegetable[x]: chosen_vegetables.append(i),
        borderwidth=5, border=2
    )
    vegetable_box.grid(row=5+row, column=col, sticky="w")

# bttn

create.grid(row=16, column=0)


root.mainloop()
