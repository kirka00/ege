s = 2 * 27 ** 7 + 3 ** 10 - 9
q = ''
while s > 0:
    q += str(s % 3)
    s //= 3
print(q.count('0'))