# 19
def f(x, p):
    if x >= 56 and p > 2:
        if x < 80:
            return p == 2
        else:
            return p == 3
    return f(x + 1, p + 1) or f(x * 3, p + 1)


print(min([i for i in range(1, 56) if f(i, 0)]))


# 20
def f(x, p):
    if x >= 56 or p > 3:
        if x < 80:
            return p == 3
        else:
            return p == 2
    if p % 2 == 0:
        return f(x + 1, p + 1) or f(x * 3, p + 1)
    else:
        return f(x + 1, p + 1) and f(x * 3, p + 1)


print(sorted([i for i in range(1, 56) if f(i, 0)]))


# 21
def f(x, p):
    if x >= 56 or p > 4:
        if x < 80:
            return p == 2 or p == 4
        else:
            return p == 1 or p == 3
    if p % 2 == 0:
        return f(x + 1, p + 1) and f(x * 3, p + 1)
    else:
        return f(x + 1, p + 1) or f(x * 3, p + 1)


print(min([i for i in range(1, 56) if f(i, 0)]))
