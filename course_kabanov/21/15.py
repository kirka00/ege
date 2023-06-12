with open('files/15.txt') as f:
	s = f.readline()
	minim = 10 ** 10
	k = ''
	for i in range(len(s)):
		if s[i] == 'D':
			k += s[i]
		elif k:
			minim = min(minim, len(k))
			k = ''
print(minim)