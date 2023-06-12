with open('files/11.txt') as f:
	s = f.readline()
	k = kmax = 1
	for i in range(len(s) - 1):
		if ''.join(sorted([s[i], s[i + 1]])) == s[i] + s[i + 1]:
			k += 1
			kmax = max(kmax, k)
		else:
			k = 1
print(kmax)