def f(x):
	n = ''
	while x > 0:
		n += str(x % 9)
		x //= 9
	return n == ''.join(sorted([j for j in n], reverse=True))


def f_2(x):
	n = ''
	while x > 0:
		n += str(x % 9)
		x //= 9
	return sum([int(q) for q in n])

for i in range(304583, 394589993):
	s = str(i)
	if s[0] == '3' and s[2:5] == '458' and s[-1] == '3' and f(i):
		print(i, f_2(i))
