with open('files/17-1.txt') as f:
	s = [int(x) for x in f]
	min_ = min([i for i in s if i > 0 and i & 15 == 0])
	ans = []
	for i in range(len(s) - 1):
		if s[i] % 2 and s[i + 1] % 2 and (s[i] + s[i + 1]) / 2 >= min_:
			ans.append((s[i] + s[i + 1]) / 2)

print(len(ans), min(ans))


# 1202 19.0