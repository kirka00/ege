with open('files/17.txt') as f:
	s = [int(x) for x in f]
	n = []
	for i in range(len(s) - 1):
		if (s[i] > 700 or s[i + 1] > 700):
			n.append(s[i] ** 2 + s[i + 1] ** 2)


print(len(n), max(n))


# 3902 197073925
