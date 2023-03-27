s = 3 ** 2017 + 9 ** 1000 + 9 ** 100 - 81
n = ''
while s > 0:
    n += str(s % 3)
    s //= 3
print(n.count('2'))


# 196 - true
