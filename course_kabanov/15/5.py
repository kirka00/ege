def three(x):
	s = ''
	while x > 0:
		s += str(x % 3)
		x //= 3
	return s


ans = []
for i in range(1, 1000):
	r = three(i)
	r += str(i % 3)
	q = int(r, 3)
	if q >= 100:
		ans.append(q)
print(min(ans))
