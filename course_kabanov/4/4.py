s = 51 * 7 ** 12 - 7 ** 3 - 22
q = ''
while s > 0:
    q += str(s % 7)
    s //= 7
print(sum([int(i) for i in q]))