k = 0
for i in range(1, 1000):
	r = bin(2 * i)[2:]
	r += str(sum([int(q) for q in r]) % 2)
	r += str(sum([int(q) for q in r]) % 2)
	q = int(r, 2)
	if q < 80:
		k += 1
print(k)
