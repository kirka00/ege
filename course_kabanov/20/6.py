with open('files/6.txt') as f:
	s = [int(x) for x in f]
	ans = []
	for i in range(len(s) - 1):
		if (s[i] + s[i + 1]) % 3 == 0 and (s[i] + s[i + 1]) % 6 != 0 and \
		abs(s[i] * s[i + 1]) % 10 == 8:
			ans.append(s[i] + s[i + 1])

print(len(ans), max(ans))