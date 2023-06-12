with open('files/12.txt') as f:
	s = [int(x) for x in f]
	ans = []
	for i in range(len(s) - 1):
		if (s[i] + s[i + 1]) >= 100 and (s[i] < 0 or s[i + 1] < 0):
			ans.append(s[i] * s[i + 1])

print(len(ans), max(ans))