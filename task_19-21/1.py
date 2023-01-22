# 19
def f(x, p):
    if x >= 100 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x + 1, p + 1) or f(x + 3, p + 1) \
            or f(x * 3, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 3, p + 1) \
            and f(x * 3, p + 1)


print(min([i for i in range(1, 100) if f(i, 1)]))


# 20
def f(x, p):
    if x >= 100 or p > 4:
        return p == 4
    if p % 2 != 0:
        return f(x + 1, p + 1) or f(x + 3, p + 1) \
            or f(x * 3, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 3, p + 1) \
            and f(x * 3, p + 1)


print([i for i in range(1, 100) if f(i, 1)])

# 21


def f(x, p):
    if x >= 100 or p > 5:
        return p == 3 or p == 5
    if p % 2 == 0:
        return f(x + 1, p + 1) or f(x + 3, p + 1) \
            or f(x * 3, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 3, p + 1) \
            and f(x * 3, p + 1)


print([i for i in range(1, 100) if f(i, 1)])
