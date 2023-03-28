with open('files/17.txt') as f:
	s = [int(x) for x in f]
	n = []
	a5 = min([i for i in s if abs(i) % 10 == 5])
	sred = sum(s) / len(s)
	for i in range(len(s) - 1):
		if abs(min(s[i], s[i + 1]) % 10 == 5) and (((s[i] ** 2) + (s[i + 1] ** 2)) < a5 ** 2):
			n.append(s[i] ** 2 + s[i + 1] ** 2)
print(len(n), max(n))


# 403 99805561
