list1 = [1,5,1,8,5]
list2 = [2,8,0]

ratio = (len(list2)/len(list1))*100
print(round(ratio))

# for i in list1:
#     print(i)
print(len(list1))
list1.pop(0)
print(list1[0])
print(len(list1))
print()
print()
print()

list2 = [{'a': [{'i': 'p'}, {'ii': 'pp'}, {'iii': 'ppp'}]}, {'b': [{'iiii': 'pppp'}, {'iiiii': 'ppppp'}]}]
for index in list2:
    print(index)
    for i in index:
        print(i)
        for p in i:
            for x in p:
                print(x)
