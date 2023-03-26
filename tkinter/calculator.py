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
    numOp.clear()


def delLast():
    current = screen.get()
    screen.delete(0, 'end')
    screen.insert(0, current[:-1])


def doOperation(operation):
    # if operation == '+':
    if screen.get()[:1] in '+-*/':
        print('operation first')

    if screen.get()[:1] == "0":
        if all(char == screen.get()[0] for char in screen.get()):
            num = screen.get()[:1]
            screen.delete(0, END)
            screen.insert(0, num)
        else:
            while screen.get()[:1] == '0':
                screen.delete(0, 1)
    if operation == "√":
        number = "1/" + screen.get()
    else:
        number = screen.get()
    print(number)
    if screen.get().isnumeric():
        numOp.append([number, operation])
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
    if len(equation) > 1:
        print(equation)
        solve = sympy.sympify(equation)
        solve2 = sympy.solve(equation)
        print(solve)
        print(solve2)
        solveStr = str(solve.evalf())
        print(solveStr)
        if solveStr != "0":
            solveStr = solveStr.rstrip('0.')
        screen.delete(0, 'end')
        screen.insert(0, solveStr)
        numOp.clear()


root = Tk()
root.title("Calculator")
root.geometry("250x400")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

screen = Entry(root, width=36, borderwidth=5, font=28)
plusBttn = Button(root, text="+", pady=20, padx=29, command=lambda i='+': doOperation(i))
minusBttn = Button(root, text="-", pady=20, padx=29, command=lambda i='-': doOperation(i))
multiBttn = Button(root, text="*", pady=20, padx=29, command=lambda i='*': doOperation(i))
diviBttn = Button(root, text="/", pady=20, padx=29, command=lambda i='/': doOperation(i))
sqrtBttn = Button(root, text="√", pady=20, padx=29, command=lambda i='√': doOperation(i))
toBttn = Button(root, text="^", pady=20, padx=29, command=lambda i='**': doOperation(i))


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
        numberPadBttn.grid(row=row, column=col, sticky="NSEW")
    else:
        numberPadBttn.grid(row=row, column=0, sticky="NSEW")

    nums = nums - 1

screen.grid(row=0, column=0, columnspan=3, sticky="NSEW", pady=8)
plusBttn.grid(row=4, column=1, sticky="NSEW")
minusBttn.grid(row=4, column=2, sticky="NSEW")
equalBttn.grid(row=5, column=0, sticky="NSEW")
multiBttn.grid(row=5, column=1, sticky="NSEW")
diviBttn.grid(row=5, column=2, sticky="NSEW")

delBttn.grid(row=6, column=0, sticky="NSEW")
clearBttn.grid(row=6, column=1, columnspan=2, sticky="NSEW")

root.mainloop()
