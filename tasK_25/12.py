i = 300_000_001
k = 0
while k != 6:
	divs = set()
	for d in range(2, round(i ** 0.5) + 1):
		if i % d == 0:
			divs.add(d)
			divs.add(i // d)
	divs = sorted(divs, reverse=True)
	ans_divs = [x for x in divs if x % 2 == 0]
	if len(ans_divs) >= 6:
		if ans_divs[5] > 0:
			k += 1
			print(ans_divs[5], len(ans_divs))
	i += 1


'''
4 7
118 7
405954 23
13636364 23
10344828 47
'''
