import logging
import tkinter
from tkinter import *

splitData = []

FORMAT = '%(asctime)s %(levelname)s %(message)s'

logging.basicConfig(
    filemode="a",
    filename="export.log",
    format=FORMAT,
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def importFile():
    try:
        with open(screen.get()+".csv", "r") as file:
            data = file.readlines()
        print(data)
        for val in data:
            splitData.append(val.strip('\n'))
    except Exception as e:
        logger.info(e, exc_info=True)
        print(e)
    print(splitData)

    if len(splitData) > 0:
        for equation in splitData:
            try:
                x, y = equation.split(',')
                print(equation)
                divide(x, y)
            except Exception as e:
                print(e)
                logger.error(e, exc_info=True)
                noExcept = 0
            else:
                noExcept = 1
    if noExcept == 1:
        print("No error detected")
        logger.info('No error detected')


def divide(x=0, y=1):
    result = 0
    try:
        print(float(x)/float(y))
    except ZeroDivisionError as e:
        print('-----------')
        logger.error(e, exc_info=True)
        print(e)
        print('-----------')
        noExcept = 0
    except Exception as e:
        print(e)
        logger.error(e, exc_info=True)
        noExcept = 0
    else:
        noExcept = 1
    finally:
        print('END')


# Basic tkinter config
root = Tk()
root.title("Divider")
root.geometry("400x250")

# row/column config
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

title = tkinter.Label(root, font=16, text="File name: ")
screen = tkinter.Entry(root, borderwidth=5, font=21)
extension = tkinter.Label(root, font=16, text=".csv")
importBttn = tkinter.Button(root, pady=10, padx=16, text="import", font=16, command=importFile)

title.grid(row=0, column=0)
screen.grid(row=0, column=1)
extension.grid(row=0, column=2)
importBttn.grid(row=1, column=1)


root.mainloop()
