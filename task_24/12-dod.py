with open('files/24-164.txt') as f:
	kmax = 0
	k = 0
	n = -1
	for s in f:
		k += 1
		c = 1
		for i in range(0, len(s)-1):
			if s[i] == s[i + 1]:
				c += 1
				if c > kmax:
					kmax = c
					n = k
			else:
				c = 1
	print(n)


with open('files/24-164.txt') as f:
	maxi = 0
	slovar = {}
	k = 0
	a = [0]*150
	for s in f.readlines():
		k += 1
		if k == 162:
			for i in range(0, len(s)):
				a[ord(s[i])] += 1
	b = []
	for i in a:
		if i != 0:
			b.append(i)
	for x in s:
		if x in slovar:
			slovar[x] += 1
		else:
			slovar[x] = 1
	alph = []
	for y in slovar.items():
		if max(slovar.values()) == y[1]:
			alph.append(y[0])

with open('files/24-s1.txt') as f:
	print(f.read().count(min(alph)))



# Z36493
