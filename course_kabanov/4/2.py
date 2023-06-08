s = 3 * 16 ** 8 - 4 ** 5 + 3
q = ''
while s > 0:
    q += str(s % 4)
    s //= 4
print(q.count('3'))