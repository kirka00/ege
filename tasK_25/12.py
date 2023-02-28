i = 300_000_001
k = 0
while k != 5:
	divs = set()
	for d in range(2, round(i ** 0.5) + 1):
		if i % d == 0:
			divs.add(d)
			divs.add(i // d)
	divs = sorted(divs, reverse=True)
	ans_divs = [x for x in divs if x % 2 == 0]
	if len(divs) >= 6:
		if divs[5] > 0:
			k += 1
			print(divs[5], len(divs))
	i += 1


'''
3 6
5 6
268 10
21428572 30
15789474 46
'''
