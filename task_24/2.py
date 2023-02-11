with open('files/24-181.txt') as f:
	s = f.readline()
	kmax = 0
	a = []
	for i in range(len(s)):
		if s[i] == '.':
			a.append(i)
	for i in range(len(a) - 5):
		kmax = max(kmax, a[i + 5] - a[i] - 1)
print(kmax)

# 483
