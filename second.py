# How to define function
x = 5


def rectangle_function(x):
    for i in range(x):
        print('')
        for a in range(x):
            print('#', end='')
    print('')
    print('')
    pass


def rectangleOutline_function(x):
    for i in range(x):
        for a in range(x):
            if i == 0 or i == x-1:
                print('#', end='')
            elif a == x-1 or a == 0:
                print('#', end='')
            else:
                print(' ', end='')
        print('')
    print('')
    pass


def pyramid_function(x):
    for i in range(x):
        for a in range(i+1):
            print('#', end='')
        print('')
    pass


def pyramidV2_function(x):
    for i in range(x):
        for a in range(i+1):
            print('#', end='')
        print('')
    pass


rectangle_function(x)
rectangleOutline_function(x)
pyramid_function(x)
print('')
pyramidV2_function(x)
