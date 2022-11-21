# How to define function
x = 10
y = 3


def rectangle_function(x):
    for i in range(x):
        print('')
        for a in range(x):
            print('#', end=' ')
    print('')
    print('')
    pass


def rectangleOutline_function(x):
    for i in range(x):
        for a in range(x):
            if i == 0 or i == x-1:
                print('#', end=' ')
            elif a == x-1 or a == 0:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')
    pass


def pyramid_function(x):
    for i in range(x):
        for a in range(i+1):
            print('#', end=' ')
        print('')
    pass


def pyramidV2_function(height):
    no = 0
    for i in range(1, height):
        for a in range(1, (height - i)):
            print(' ', end=' ')
        while no != ((2 * i) - 1):
            print('#', end=' ')
            no += 1
        no = 0
        print('')
    pass


def cross_function(length):
    lines = length
    for i in range(1, length+1):
        print('')
        for a in range(1, length+1):
            if i == a or lines == a:
                print('#', end='')
            else:
                print(' ', end='')
        lines -= 1
    pass


def diamond_function(side):
    side += 1
    no = 0
    for i in range(1, side):
        for a in range(1, (side - i)):
            print(' ', end=' ')
        while no != ((2 * i) - 1):
            print('#', end=' ')
            no += 1
        no = 0
        print('')
    no2 = 0
    for i in reversed(range(1, side-1)):
        for a in reversed(range(1, (side - i))):
            print(' ', end=' ')
        while no2 != ((2 * i) - 1):
            print('#', end=' ')
            no2 += 1
        no2 = 0
        print('')
    pass


def circle_function(radius):
    no = 0
    for i in range(1, radius-1):
        for a in range(1, (radius - i)):
            print(' ', end='  ')
        while no != ((2 * i)+(radius-6)):
            print('#', end='  ')
            no += 1
        no = 0
        print('')
    for i in range((radius-6)):
        print(' ', end='  ')
        for a in range(radius*2):
            print('#', end='  ')
        print('')
    for i in reversed(range(1, radius - 1)):
        for a in range(1, (radius - i)):
            print(' ', end='  ')
        while no != ((2 * i)+(radius-6)):
            print('#', end='  ')
            no += 1
        no = 0
        print('')

    pass


def chessBoard_function(side):
    for i in range(side):
        print('')
        for a in range(side):
            if i % 2 != 0:
                if a % 2 != 0:
                    print('#', end=' ')
                else:
                    print('`', end=' ')
            else:
                if a % 2 != 0:
                    print('`', end=' ')
                else:
                    print('#', end=' ')
            # jestli je i sudy tak a bude mit # liche a . sude, pokud je i liche tak # bude sudy a . liche
    pass


def chessBoardV2_function(side, size):
    for i in range(side):
        for p in range(size):
            print('')
            for a in range(side):
                if i % 2 != 0:
                    if a % 2 != 0:
                        for c in range(size):
                            print('#', end=' ')
                    else:
                        for u in range(size):
                            print('`', end=' ')
                else:
                    if a % 2 != 0:
                        for m in range(size):
                            print('`', end=' ')
                    else:
                        for n in range(size):
                            print('#', end=' ')
    pass


rectangle_function(x)
rectangleOutline_function(x)
pyramid_function(x)
print('')
pyramidV2_function(x)
print('')
cross_function(x)
print('')
diamond_function(x)
print('')
circle_function(x)
print('')
chessBoard_function(x)
print('')
chessBoardV2_function(x, y)
