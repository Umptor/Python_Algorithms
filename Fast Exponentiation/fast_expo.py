def get_2_expos(y):
    if y < 2:
        return [1]

    biggest = 2
    while biggest < y:
        biggest *= 2

    biggest /= 2
    expos = []
    initial = y
    while biggest != 1:
        if biggest <= y:
            expos.append(1)
            y -= biggest
        else:
            expos.append(0)


        biggest /= 2

    if initial % 2 == 1:
        expos.append(1)
    else:
        expos.append(0)
    expos.reverse()

    return expos



def fast_expo(x, y, n):
    r = 1
    b = x

    expos = get_2_expos(y)
    value = 1
    print('exponents=', expos)
    print('r=', 'bsey', 'b=', x % n)
    for expo in expos:
        if pow(expo, value) == 1:
            r = (r * b) % n

        b = (b*b) % n
        print('r=', r, 'b=', b)
        value *= 2

    return r


def solve():
    # base
    x = 2
    # exponent
    y = 11
    # mod
    n = 67

    print('ans = ', fast_expo(x, y, n))
    print('real ans = ', pow(x, y) % n)


def find_generator():
    # base
    x = 2
    # exponent
    y = 11
    # mod
    n = 67

    result = 0

    while result != 1:
        print('ans = ', fast_expo(x, y, n))
        x += 1



find_generator()
