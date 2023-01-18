def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(int('1' + str(x)), y)


print(f(1, 512))
