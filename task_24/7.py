with open('files/24.txt') as f:
	s = f.readline()
	k = kmax = 1
	w, maxw = s[0] , ''
	for i in range(1, len(s)):
		if s[i] < s[i - 1]:
			k += 1
			w += s[i]
			if k > kmax:
				kmax = k
				maxw = w
		else:
			k = 1
			w = s[i]
print(maxw, kmax)


# ZYX 3
