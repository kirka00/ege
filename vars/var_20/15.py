def f(x, y):
    return (y + 2 * x <= 27) <= (y - x > 3) or (y <= a)


for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break


# 11 - true
