def f(x, y):
    return ((x < a) and (y < a) and (x * y > 1200))

for a in range(1000):
    if not (any(f(x, y) for x in range(1000) for y in range(1000))):
        print(a)

# 35
# any = false