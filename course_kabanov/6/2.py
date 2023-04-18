def f(x):
    return (((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0))


for a in range(1, 100000):
    if all(f(x) for x in range(1,3000)):
        print(a)
        break


# 1260
