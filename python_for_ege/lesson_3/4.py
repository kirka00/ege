n, a, b = int(input()), 0, 1
for i in range(1, n + 1):
    a += i
    b *= a
print(b)
