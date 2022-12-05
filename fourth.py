list5 = list(range(1, 6))
print(list5)
list6 = ["test1", "test2", "test3"]

print(list6)


class ClassOne:
    def __int__(self, val):
        self.val = val


# x = ClassOne('Firsst value')
# print(x.val)

list6.append(5)
print(list6)
list6.pop()
print(list6)
len(list6)
print(len(list6))
list7 = ['Anička', "Luboš", "Zdeněk", "Bořivoj"]
list8 = ["ě", "š", "č", "ř", "ž", "ý", "á", "í", "é", "ú", "ů", "ó"]
list9 = ["e", "s", "c", 'r', 'z', 'y', 'a', 'i', 'e', 'u', 'u', 'o']
for i in list7:  # name
    for x in i:  # char
        print(i)
        for z in list8:
            if x == z:
                print(list8.index(x))
                print(list9.index(x))
                # res = i.replace(list9[list8.index(x), list8.index(x)])

print(list7)

# import unidecode.unidecode(string)
