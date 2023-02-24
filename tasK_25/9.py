i = 650_001
k = 0
while k != 7:
	divs = set()
	for d in range(2, round(i ** 0.5) + 1):
		if i % d == 0:
			divs.add(d)
			divs.add(i // d)
	if len(divs) != 0:
		if sum(divs) % 37 == 23:
			k += 1
			print(i, sum(divs))
	i += 1


'''
650031 237008
650130 1031213
650160 1968719
650187 366212
650210 687261
650298 801221
650304 1215325
'''
