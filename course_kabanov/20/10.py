with open('files/10.txt') as f:
	s = [int(x) for x in f]
	ans = []
	for i in range(len(s) - 2):
		if s[i] % 3 == 2 or s[i + 1] % 3 == 2 or s[i + 2] % 3 == 2:
			ans.append(min(s[i], s[i + 1], s[i + 2]))

print(len(ans), sum(ans))