for i in range(1, 1000):
	r = bin(i)[2:]
	if i % 2 == 0:
		r += '01'
	else:
		r += '10'
	q = int(r, 2)
	if q > 81:
		print(q)
		break

    