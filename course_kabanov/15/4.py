for i in range(1, 1000):
	r = bin(i)[2:]
	r += r[-1]
	if r.count('1') % 2 == 0:
		r += '0'
	else:
		r += '1'
	if r.count('1') % 2 == 0:
		r += '0'
	else:
		r += '1'
	q = int(r, 2)
	if q > 144:
		print(q)
		break
