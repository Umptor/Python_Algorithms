def eucledean(a, b):

    print(a, b)

    if a <= 1:
        return b
    if b <= 1:
        return a

    return eucledean(abs(b), a % b)


print('ans', eucledean(840, 11))
