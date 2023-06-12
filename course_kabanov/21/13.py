with open('files/13.txt') as f:
	s = f.readline()
	k = kmax = ''
	for i in range(1, len(s)):
		if s[i - 1] > s[i]:
			k += s[i]
			kmax = max(kmax, k, key=len)
		else:
			k = s[i]
print(kmax)