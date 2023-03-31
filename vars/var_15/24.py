with open('files/24.txt') as f:
	s = f.readline()
	k = kmax = 1
	for i in range(len(s)):
		if s[i] != s[i - 1]:
			k += 1
			kmax = max(k, kmax)
		else:
			k = 1
print(kmax)


# 120
