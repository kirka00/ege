for n in range(1000):
	r = bin(n)[2:]
	if sum([int(i) for i in r]) % 4 == 0:
		r += '10'
	else:
		r += '11'
	if int(r[-1]) % 2:
		r += '0'
	else:
		r += '1'
	if int(r, 2) <= 250:
		print(n)


# 30