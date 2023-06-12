with open('files/15.txt') as f:
	s = [int(x) for x in f]
	ans = []
	max_ = max([i for i in s if i % 19 == 0])
	for i in range(len(s) - 1):
		if s[i] > max_ or s[i + 1] > max_:
			ans.append(s[i] + s[i + 1])

print(len(ans), min(ans))	