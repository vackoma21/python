from tkinter import *
import math
import sympy

numOp = []

# solution for when user inputs operation first

def putNumber(number):
    # print(number)
    current = screen.get()
    if current[:1] in '+-*/' or not current.isnumeric():
        screen.delete(0, END)
        current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))
    print(numOp)


def clearScreen():
    screen.delete(0, 'end')


def delLast():
    current = screen.get()
    screen.delete(0, 'end')
    screen.insert(0, current[:-1])


def doOperation(operation):
    # if operation == '+':
    if screen.get()[:1] in '+-*/':
        print('operation first')
    while screen.get()[:1] == '0':
        screen.delete(0, 1)
        print('ZERO')
    numOp.append([screen.get(), operation])
    screen.delete(0, 'end')
    screen.insert(0, operation)
    print(operation)


def calculate():
    solve = ''
    lastNum = screen.get()
    if lastNum in '+-/*':
        lastNum = '0'
    equation = ''
    for val in numOp:
        equation = equation + val[0] + val[1]
    equation = equation + lastNum
    print(equation)
    solve = sympy.sympify(equation)
    solve2 = sympy.solve(equation)
    print(solve)
    print(solve2)
    screen.delete(0, 'end')
    screen.insert(0, solve)
    numOp.clear()


root = Tk()
root.title("Calculator")

screen = Entry(root, width=36, borderwidth=5)
plusBttn = Button(root, text="+", pady=20, padx=29, command=lambda i='+': doOperation(i))
minusBttn = Button(root, text="-", pady=20, padx=29, command=lambda i='-': doOperation(i))
multiBttn = Button(root, text="*", pady=20, padx=29, command=lambda i='*': doOperation(i))
diviBttn = Button(root, text="/", pady=20, padx=29, command=lambda i='/': doOperation(i))


dec_pointBttn = Button(root, text='.', pady=20, padx=29, command=lambda j='.': putNumber(j))

equalBttn = Button(root, text="=", pady=20, padx=29, command=calculate)
clearBttn = Button(root, text="CE", pady=20, padx=80, command=clearScreen)
delBttn = Button(root, text='del', pady=20, padx=25, command=delLast)

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
multiBttn.grid(row=5, column=1)
diviBttn.grid(row=5, column=2)

delBttn.grid(row=6, column=0)
clearBttn.grid(row=6, column=1, columnspan=2)

root.mainloop()
