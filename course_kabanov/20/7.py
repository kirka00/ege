with open('files/7.txt') as f:
	s = [int(x) for x in f]
	ans = []
	for i in range(len(s) - 1):
		if (s[i] + s[i + 1]) % 7 == 0 and s[i] * s[i + 1] > 0:
			ans.append(s[i] * s[i + 1])

print(len(ans), min(ans))