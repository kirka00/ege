with open('files/23.txt') as f:
	s = f.readline()
	kmax = 0
	for i in range(3):
		k = 0
		for j in range(i, len(s) - 2, 3):
			if (s[j] == 'A' and s[j + 2] == 'A') or \
			(s[j] == 'C' and s[j + 2] == 'C'):
				k += 1
				kmax = max(kmax, k)
			else:
				k = 0
print(kmax)

