with open('files/8.txt') as f:
	s = [int(x) for x in f]
	ans = []
	for i in range(len(s) - 2):
		if abs(s[i] + s[i + 1] + s[i + 2]) % 10 == 5 and s[i] * s[i + 1] * s[i + 2] % 7 == 0:
			ans.append(s[i] + s[i + 1] + s[i + 2])

print(len(ans), max(ans))