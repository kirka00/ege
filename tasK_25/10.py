i = 500_000_001
k = 0
while k != 5:
	divs = set()
	for d in range(2, round(i ** 0.5) + 1):
		if i % d == 0:
			divs.add(d)
			divs.add(i // d)
	divs = sorted(divs)
	if len(divs) >= 5:
		p = divs[0] * divs[1] * divs[2] * divs[3] * divs[4]
		if p <= i and p % 100 == 91:
			k += 1
			print(p, divs[4])
	i += 1

'''
56401891 139
74342691 1259
149721291 531
375291 37
267817291 203
'''
