with open('files/12.txt') as f:
	s = f.readline()
	k = kmax = 1
	for i in range(1, len(s)):
		if s[i] > s[i - 1]:
			k += 1
			kmax = max(kmax, k)
		else:
			k = 1
print(kmax)