from tkinter import *
import math


def putNumber(number):
    print(number)
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))


def doOperation(operation):
    if operation == '+':


root = Tk()
root.title("Calculator")

screen = Entry(root, width=36, borderwidth=5)
plusBttn = Button(root, text="+", pady=20, padx=29, command=lambda i='+': doOperation(i))
minusBttn = Button(root, text="-", pady=20, padx=30, command=lambda i='-': doOperation(i))
equalBttn = Button(root, text="=", pady=20, padx=30)
clearBttn = Button(root, text="CE", pady=20, padx=63)

col = 3
nums = 9
for x in range(1, nums+2):
    if col == 0:
        col = 2
    else:
        col = col - 1
    row = math.ceil(x/3)

    numberPadBttn = Button(root, text=nums, pady=20, padx=30, command=lambda j=nums: putNumber(j))

    if nums != 0:
        numberPadBttn.grid(row=row, column=col)
    else:
        numberPadBttn.grid(row=row, column=0)

    nums = nums - 1

screen.grid(row=0, column=0, columnspan=3)
plusBttn.grid(row=4, column=1)
minusBttn.grid(row=4, column=2)
equalBttn.grid(row=5, column=0)
clearBttn.grid(row=5, column=1, columnspan=2)

root.mainloop()
