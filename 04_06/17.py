with open('files/17.txt') as f:
	summa_ = sum([int(i) for i in f])
	ans = []
	s = [int(x) for x in f]
	for i in range(len(s) - 1):
		if (s[i] % 100 == 10 and s[i + 1] % 100 != 10 and s[i] + s[i + 1] < summa_) or \
		(s[i] % 100 != 10 and s[i + 1] % 100 == 10 and s[i] + s[i + 1] < summa_):
			ans.append(s[i] + s[i + 1])


print(len(ans), min(ans))