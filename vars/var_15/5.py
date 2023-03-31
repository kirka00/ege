for n in range(1, 1000):
	r = bin(n)[2:]
	q = ''
	for i in r:
		if i == '0':
			q += '00'
		else:
			q += '11'
	r = int(q, 2)
	if r > 32:
		print(r)
		break


# 48
