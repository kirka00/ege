def f(x, y, p):
    if x + y >= 59 or p > 2:
        return p == 2
    if p % 2:
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and \
        f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or \
f(x, y * 2, p + 1)
        

print(([i for i in range(54) if f(5, i, 0)]))