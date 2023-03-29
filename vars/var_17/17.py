with open('files/17.txt') as f:
	s = [int(x) for x in f]
	n = []
	for i in range(len(s) - 1):
		if s[i] < 450 and s[i + 1] < 450:
			n.append(s[i] ** 3 + s[i + 1] ** 3)
print(len(n), max(n))


# 1533 81262125 - true
