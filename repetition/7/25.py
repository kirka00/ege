def divchet(a):
	d = set()
	for i in range(1, round(a ** 0.5) + 1):
		if a % i == 0:
			d.add(i)
			d.add(a // i)
	return len([x for x in d if x % 2 == 0])


k = 0
count = 0
while count != 5:
	chet = divchet(750_000 + k)
	if chet % 2:
		count += 1
		print(k, chet)
	k += 1


'''
1538 3
3992 9
6450 27
8912 63
11378 3
'''