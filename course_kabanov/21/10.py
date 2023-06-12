with open('files/10.txt') as f:
	s = f.readline()
	k = kmax = 1
	for i in range(len(s) - 1):
		if s[i] != s[i + 1]:
			k += 1
			kmax = max(kmax, k)
		else:
			k = 1
print(kmax)