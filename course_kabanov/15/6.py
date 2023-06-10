for i in range(1, 100):
	r = bin(i)[2:]
	r = r[::-1]
	r = r[r.index('1'):]
	q = int(r, 2)
	if q == 13:
		print(i)
