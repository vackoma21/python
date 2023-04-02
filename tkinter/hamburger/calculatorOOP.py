from tkinter import *


class Calculator:
    def __init__(self, root):
        operators = ["+", "-", "*", "/", "√", "**"]

        self.screen = Entry(root,
               width=36, borderwidth=5, font=28,
               bg="#202020", fg="#E0E0E0",
               relief="solid", insertbackground='white')
    def operatorBttns(self, root):
