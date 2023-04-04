s = 64 ** 30 + 2 ** 300 - 4
n = ''
while s > 0:
    n += str(s % 8)
    s //= 8
print(n.count('7'))


# 59
