with open('files/22.txt') as f:
	s = f.readline()
	kmax = 0
	for i in range(3):
		k = 0
		for j in range(i, len(s) - 2, 3):
			if s[j] in '12' and s[j + 1] in '12' and \
			s[j + 2] in 'AB':
				k += 1
				kmax = max(kmax, k)
			else:
				k = 0
print(kmax)

