# *, /, -, +
# print('First line of code written out by print')
# print('Second lined -,,-')
# before function, 2 empty lines
# Python is key-sensitive
# basic mathematical operations
# + - * /
# diversion 7//2 = 2
# modulo 12 % 5 = 2
# 2 ** 5 | 2*2*2*2*2
# 32 ** 1/5
# variable
variable = "Variable"
variable = 5
print(variable)
x, y, z = 3, 73.5, 'hi'
print(x, y, z)
str()
int()
bool()
isinstance(x, int)  # True
print(isinstance(x, int))
float(2.1)
float(2.5)
print(int(2.1))  # takes just the whole number, decimal places are deleted
print(int(2.5))
round(2.5, 0)
print(round(2.5, 0))
bool()
# size = 1
# size == 1
# size < 2
# size > 1

# fre
# erg
# rgw    command + / to comment more lines of code/text
# vfd
# b

# AND, OR
# False = 0, True = 1
#

# userInput = input("Write some text: ")
# number = input("Write a number: ")
#
# print('Hello ' + "World")
# print(
#     'reg'
#     'wef'
#     'greg'
# )
# print(userInput * int(number))

# IN: whole number n > 0
# OUT: S and o of a square
no = input("Write a whole number: ")
obsah = int(no)*int(no)
obvod = 4*int(no)
print('Number:', no)
print("Obvod:", str(obvod) + 'cm', 'Obsah:', str(obsah) + 'cmˆ2')

print(f"Obvod: {obvod} cm, Obsah: {obsah} cmˆ2")
# f before string = format

# If else statement

if 1 > 0:
    print('1 is bigger then 0')

inputTwo = input("Type number smaller than 8: ")
if int(inputTwo) < 8:
    print("Good job")
else:
    # pass = nothing is gonna happen
    pass

# Cycles
# for, while
# while checks statement before running, do while checks statement in the end

for i in range(10):
    print(i)
i = 10
while i > 0:
    print(i)
    i -= 1
    # i = i+1

slovo = "Python"
for i in slovo:
    print(i)

samohlasky = 0
souhlasky = 0
cisla = 0
ostatni = 0
word = input("Write a word: ")
for char in word:
    if char in "aeiouy":
        samohlasky = samohlasky + 1
    elif char in "qwrtypsdfghjklxcvbnm":
        souhlasky += 1
    elif char in "0123456789":
        cisla += 1
    else:
        ostatni += 1
print(f"Word, {word}, has {samohlasky} samohlasek")
print(f"Word, {word}, has {souhlasky} souhlasek")
print(f"Word, {word}, has {cisla} numbers")
print(f"Word, {word}, has {ostatni} other characters")