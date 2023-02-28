i = 10_000_001
k = 0
while k != 5:
	divs = set()
	for d in range(2, round(i ** 0.5) + 1):
		if i % d == 0:
			divs.add(d)
			divs.add(i // d)
	divs = sorted(divs, reverse=True)
	if len(divs) >= 3:
		p = divs[0] + divs[1] + divs[2]
		if str(p).count('7') >= 4:
			k += 1
			print(p)
	i += 1


'''
2772677
8750777
7501777
3377771
7772735
'''
