s = 5 ** 28 + 25 ** 6 - 125
n = ''
while s > 0:
    n += str(s % 5)
    s //= 5
print(n.count('4'))


# 9
