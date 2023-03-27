def f(x, y):
    return (y + 5 * x <= 34) <= (y - x > 4) or (y <= a)


for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break


# 9 - true
