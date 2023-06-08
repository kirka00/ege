s = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
q = ''
while s > 0:
	q += str(s % 12)
	s //= 12
print(q.count('11')) #  B = 11