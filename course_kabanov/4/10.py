s = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
q = ''
while s > 0:
	q += str(s % 6)
	s //= 6
print(q.count('5') - q.count('0'))