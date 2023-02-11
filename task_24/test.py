with open('files/24-157.txt') as f:
	s = f.readline()
	k = kmax = 0
	for i in range(len(s) - 1):
		if s[i] == 'Q' and s[i + 1] == 'W':
			k = 1
		else:
			k += 1
			kmax = max(kmax, k)

print(kmax)
