def f(x):
    return ((x & 116 != 0) or (x & 92 != 0)) <= ((x & 69 == 0) <= (x & a != 0))


for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
    

# 56