def f(x, y):
    if x < y or x == 22:
        return 0
    if x == y:
        return 1
    return f(x - 2, y) + f(x // 2, y) + f(x // 3, y)


print(f(40, 2))


# 260