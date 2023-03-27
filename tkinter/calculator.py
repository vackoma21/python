from tkinter import *
import math
import sympy

# save numbers and operators inside a list
numOp = []
# holds the **(1/2) if presssed
cacheOp = []

validKeys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "+", "-", "*", "^", "(", ")"]


# displays clicked number to the screen
def putNumber(number):
    # print(number)
    current = screen.get()
    if current[:1] in '+-*/' or not current.isnumeric():
        screen.delete(0, END)
        current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))


# function that clears the screens input
def clearScreen():
    screen.delete(0, 'end')
    numOp.clear()


# function to delete last char on the screen
def delLast():
    current = screen.get()
    screen.delete(0, 'end')
    screen.insert(0, current[:-1])


# adds num inserted onto the screen and appends it to
# a numOp list together with the operator
def doOperation(operation):
    if screen.get()[:1] == "0":
        # checks if all chars on the screen are '0'
        if all(char == screen.get()[0] for char in screen.get()):
            num = screen.get()[:1]
            screen.delete(0, END)
            screen.insert(0, num)
        else:   # not all chars on the screen are '0'
            # removes all unnecessary zeros
            while screen.get()[:1] == '0':
                screen.delete(0, 1)
    # save the "√" if user inputs it into cacheOp
    if operation == "√":
        operation = "**(1/2)"
        cacheOp.append(operation)
        return 'break'
    else:   # operation isn't "√"
        number = screen.get()
    # if user inputted a number and operation isn't "√"
    if screen.get().isnumeric() and len(cacheOp) == 0:
        numOp.append([number, operation])
    # user inputted operation "√", delete it from cacheOp,
    # append the operation only, othe leave blank
    elif len(cacheOp) > 0:
        numOp.append([number, cacheOp[0]])
        cacheOp.pop(0)
        numOp.append([operation, ""])
    # clear the screen
    screen.delete(0, 'end')


# solves the created equation
def calculate():
    lastNum = screen.get()
    # if user inputs op. sign at the end
    if lastNum in '+-/*^':
        lastNum = ''
    # for cases when the user types in the equation
    if len(screen.get()) != 0:
        if lastNum[-1] in '+-/*^':
            lastNum = lastNum[:-1] + ''
    equation = ''
    for val in numOp:
        equation = equation + val[0] + val[1]
    if len(cacheOp) == 0:
        equation = equation + lastNum
    else:
        equation = equation + lastNum + cacheOp[0]
        cacheOp.clear()

    if len(equation) > 0:
        equation = equation.replace("^", "**")
        if equation[-1] in '+-/*^':
            equation = equation[:-1]

        solve = sympy.sympify(equation)
        solveStr = str(solve.evalf())
        if solveStr != "0":
            solveStr = solveStr.rstrip('0.')
        screen.delete(0, 'end')
        screen.insert(0, solveStr)
        numOp.clear()


def keyNumber(key):
    current = screen.get()
    screen.delete(0, END)
    if key.char in validKeys or key.keysym == "BackSpace":
        screen.insert(0, current)
    elif key.keysym == "Return":
        screen.insert(0, current)
        calculate()
    elif key.keysym == ("Left" or "Right"):
        screen.insert(0, current)
    else:
        screen.insert(0, current)
        return 'break'


root = Tk()
root.title("Calculator")
root.geometry("250x400")
root.configure(bg="#404040")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

screen = Entry(root,
               width=36, borderwidth=5, font=28,
               bg="#202020", fg="#E0E0E0",
               relief="solid", insertbackground='white')
screen.bind('<Key>', keyNumber)

plusBttn = Button(root,
                  text="+", pady=20, padx=29, font=21,
                  relief="solid", borderwidth=3, bg="#202020", fg="#E0E0E0",
                  activebackground='#202020', activeforeground="#E0E0E0",
                  command=lambda i='+': doOperation(i))
minusBttn = Button(root,
                   text="-", pady=20, padx=29, font=21,
                   relief="solid", borderwidth=3, bg="#202020", fg="#E0E0E0",
                   activebackground='#202020', activeforeground="#E0E0E0",
                   command=lambda i='-': doOperation(i))
multiBttn = Button(root,
                   text="*", pady=20, padx=29, font=21,
                   relief="solid", borderwidth=3, bg="#202020", fg="#E0E0E0",
                   activebackground='#202020', activeforeground="#E0E0E0",
                   command=lambda i='*': doOperation(i))
diviBttn = Button(root,
                  text="/", pady=20, padx=29, font=21,
                  relief="solid", borderwidth=3, bg="#202020", fg="#E0E0E0",
                  activebackground='#202020', activeforeground="#E0E0E0",
                  command=lambda i='/': doOperation(i))
sqrtBttn = Button(root,
                  text="√", pady=20, padx=29, font=21,
                  relief="solid", borderwidth=3, bg="#202020", fg="#E0E0E0",
                  activebackground='#202020', activeforeground="#E0E0E0",
                  command=lambda i='√': doOperation(i))
toBttn = Button(root,
                text="^", pady=20, padx=29, font=21,
                relief="solid", borderwidth=3, bg="#202020", fg="#E0E0E0",
                activebackground='#202020', activeforeground="#E0E0E0",
                command=lambda i='**': doOperation(i))

# dec_pointBttn = Button(root, text='.', pady=20, padx=29, command=lambda j='.': putNumber(j))

equalBttn = Button(root,
                   text="=", pady=20, padx=29, font=21,
                   relief="solid", borderwidth=3, bg="#202020", fg="#E0E0E0",
                   activebackground='#202020', activeforeground="#E0E0E0",
                   command=calculate)
clearBttn = Button(root,
                   text="CE", pady=20, padx=25, font=21,
                   relief="solid", borderwidth=3, bg="#202020", fg="#E0E0E0",
                   activebackground='#202020', activeforeground="#E0E0E0",
                   command=clearScreen)
delBttn = Button(root,
                 text='del', pady=20, padx=25, font=21,
                 relief="solid", borderwidth=3, bg="#202020", fg="#E0E0E0",
                 activebackground='#202020', activeforeground="#E0E0E0",
                 command=delLast)

col = 3
nums = 9
for x in range(1, nums+2):
    if col == 0:
        col = 2
    else:
        col = col - 1
    row = math.ceil(x/3)

    numberPadBttn = Button(root,
                           text=nums, pady=20, padx=30, font=21,
                           borderwidth=3, relief="solid", bg="#202020", fg="#E0E0E0",
                           activebackground='#202020', activeforeground="#E0E0E0",
                           command=lambda j=nums: putNumber(j))

    if nums != 0:
        numberPadBttn.grid(row=row, column=col, sticky="NSEW")
    else:
        numberPadBttn.grid(row=row, column=0, sticky="NSEW")

    nums = nums - 1

screen.grid(row=0, column=0, columnspan=4, sticky="NSEW", pady=8)
plusBttn.grid(row=4, column=1, sticky="NSEW")
minusBttn.grid(row=4, column=2, sticky="NSEW")
equalBttn.grid(row=5, column=0, sticky="NSEW")
multiBttn.grid(row=5, column=1, sticky="NSEW")
diviBttn.grid(row=5, column=2, sticky="NSEW")
sqrtBttn.grid(row=1, column=3, sticky="NSEW")
toBttn.grid(row=2, column=3, sticky="NSEW")

# dec_pointBttn.grid(row=3, column=3, sticky="NSEW")

delBttn.grid(row=3, column=3, sticky="NSEW")
clearBttn.grid(row=4, column=3, rowspan=2, sticky="NSEW")

root.mainloop()
