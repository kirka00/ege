with open('files/17.txt') as f:
	s = [int(x) for x in f]
	n = []
	for i in range(len(s) - 1):
		if 50 <= (abs(s[i]) + abs(s[i + 1])) <= 200:
			n.append(min(s[i], s[i + 1]))

print(len(n), min(n))


# 1 -92 - true
