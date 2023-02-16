with open('24var05-08.txt') as f:
	s = f.readline()
	k = kmax = 1
	for i in range(1, len(s)):
		if s[i - 1] + s[i] in ('12', '21', '13', '31'):
			k = 1
		else:
			k += 1
			kmax = max(kmax, k)
print(kmax)



# 339 - true
