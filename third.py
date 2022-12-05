x, y = 0, 1
z, q = 0, 1
while x < 100:
    print(x)
    x, y = y, x+y

list1 = [1, 2, 3, "Hello", "World"]
print(list1)

list2 = list(range(7, 71, 7))
print(list2)

list3 = [4, 7, 2, 8, 1, 8, 9, 3, 5, 6, 2, 7, 4, 1, 2]
print(min(list3))
print(max(list3))
print(sorted(list3))
print(sum(list3))
print()


def sumThis_function(val):
    x = 0
    for i in val:
        x = x+val[i]
    return x


print(sumThis_function(list3))


def min_function(val):
    listnew = val[0]
    for i in val:
        if val[i] < listnew:
            listnew = val[i]
    return listnew


print(min_function(list3))