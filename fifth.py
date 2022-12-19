# fce na zjisteni prvocisla

def primeNumber(num):
    notPrime = []
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


def primeNo2_fce():
    primes = []
    for p in range(1, 1000):
        if p > 1:
            for i in range(2, p):
                if p % i == 0:
                    #  return 'is not prime number'
                    pass
            else:
                primes.append(p)
        else:
            #  return 'is not prime number'
            pass


# num = int(input('Write a whole number: '))
# print(num, primeNumber(num))
#
# list_of_numbers = [654, 235, 7, 21, 9, 3579, 23, 98, 1]
#
# for i in list_of_numbers:
#     print(i, primeNumber(i))
#
# list_of_strings = ['gergw', 'qgonbfkenvow', 'gpqsdmg', 'plqnai', 'qgnoreg']
# list_of_txt = list(('AAA', 'BBBB'))
#
# for i in range(len(list_of_numbers)):
#     print(list_of_numbers[i], primeNumber(list_of_numbers[i]))
def printList_fce(x):
    for i in x:
        print(i, end=' ')
    print()
    pass


# cars = [
#     'Ford',
#     'Audi',
#     'Skoda',
#     'Opel'  # last item in list can end with ,
# ]
#
# print(cars)  # chybny vypis, pouze var_dump
# cars.append('Ferrari')
#
# cars.insert(1, 'Volkswagen')
# cars.insert(len(cars), 'Volkswagen')
# cars.insert(-1, 'Mazda')  # -1 second to last
#
# printList_fce(cars)
# del cars[3]
# cars.remove('Opel')
#
# printList_fce(cars)
#
# print(cars.index('Ferrari'))
# cars.reverse()
# print(cars)
#
# last_car = cars.pop(-1)
# print(last_car)

# wrong, the file needs to be closed, at the end needs to be closed soubor.close()
# soubor = open("words.txt", "r")
# print(soubor.read())
# print(soubor.readline())
# with open("words.txt") as f:
#     # f.readline(), at the end is always \n, fce to correct this: words. strip('\n')
#     words = f.read().splitlines()
# with open("difficultWords.txt") as f:
#     difficultWords = f.read().splitlines()

# dont use word GLOBAL for declaring global variables

primeNo = []
for i in range(1000):
    if primeNumber(i):
        primeNo.append(i)

print(printList_fce(primeNo))

# list comprehension

numbers = [i for i in range(1000)]

numbersTwo = [i for i in range(1000) if primeNumber(i)]

binary = [2 ** i for i in range(1000)]

# print(binary)
o = 1
times = [[o*p for o in range(1, 10)] for p in range(1, 10)]
# print(times)
for i in range(1, 10):
    for p in range(1, 10):
        print(i*p, end=' ')
    print()

# W: 2 dimensional array/list

primeNo_numbers = [i for i in range(1000) if primeNumber(i)]
primeNo_divider = [[4, 2], [12, 2, 3, 4, 6]]
# print(primeNo_divider)

# tabulka, starts with 1 and ends with 9
