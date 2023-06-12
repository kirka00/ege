with open('files/18.txt') as f:
	s = [int(x) for x in f]
	ans = []
	for i in range(len(s) - 1):
		if (s[i] % 9 == 0 and s[i + 1] % 9 and abs(s[i + 1]) % 8 == 3) or \
			(s[i + 1] % 9 == 0 and s[i] % 9 and abs(s[i]) % 8 == 3):
			ans.append(max(s[i], s[i + 1]))
print(len(ans), max(ans))