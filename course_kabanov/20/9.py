with open('files/9.txt') as f:
	s = [int(x) for x in f]
	ans = []
	for i in range(len(s) - 2):
		if (s[i] % 12 == 0 or s[i + 1] % 12 == 0 or s[i + 2] % 12 == 0) \
			and s[i] % 3 == 0 and s[i + 1] % 3 == 0 and s[i + 2] % 3 == 0:
			ans.append((s[i] + s[i + 1] + s[i + 2]) // 3)

print(len(ans), min(ans))