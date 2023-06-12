with open('files/19.txt') as f:
	s = f.readline()
	kmax = 0
	for i in range(2):
		k = 0
		for j in range(i, len(s) - 1, 2):
			if s[j] in 'BCD' and s[j + 1] in 'AO':
				k += 1
				kmax = max(kmax, k)
			else:
				k = 0
print(kmax)