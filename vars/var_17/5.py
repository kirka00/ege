for n in range(1, 1000):
	q = ''
	r = bin(n)[2:]
	for i in r:
		if i == '0':
			q += '01'
		else:
			q += '10'
	r = int(q, 2)
	if r > 63:
		print(r)
		break


# 149 - true
