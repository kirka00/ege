k = 0
for i in range(2, 1000):
    x = i
    if x % 2 == 0:
        x // 2
    else:
        x -= 1
    if x % 3 == 0:
        x // 3
    else:
        x -= 1
    if x % 5 == 0:
        x // 5
    else:
        x -= 1
    if x == 3:
        k += 1
print(k)
