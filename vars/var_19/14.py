s = 3 ** 2017 + 9 ** 1000 - 27
n = ''
while s > 0:
    n += str(s % 3)
    s //= 3
print(n.count('2'))


# 1997 - true
