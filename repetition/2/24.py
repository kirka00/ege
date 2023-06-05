with open('files/24.txt') as f:
	s = f.readline()
	k = kmax = 3
	for i in range(len(s) - 3):
		if s[i:i+4] == 'XZZY':
			kmax = max(k, kmax)
			k = 3
		else:
			k += 1
	print(kmax)

# 1713