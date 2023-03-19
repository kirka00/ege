with open('files/dz_4/b.txt') as f:
	n = int(f.readline())
	B, D = 10, 6
	dmin = 10 ** 10
	s = 0
	for i in range(n):
		a, b  =map(int, f.readline().split())
		s += min(a, b)
		d = abs(a - b)
		r = d % B
		if r != 0:
			dmin = min(d, dmin)
	if s % B != D:
		print(s)
	else:
		print(s, s % B, dmin)
		print(s + dmin)


# 8015 19596697
