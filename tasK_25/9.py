i = 650_001
k = 0
while k != 4:
	divs = set()
	for d in range(2, round(i ** 0.5) + 1):
		if i % d == 0:
			divs.add(d)
			divs.add(i // d)
	if len(divs):
		if sum(divs) // len(divs) % 37 == 23:
			k += 1
			print(i, sum(divs) // len(divs))
	i += 1


'''
650055 19189
650062 34618
650089 11123
650090 24295
'''
