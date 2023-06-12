with open('files/17.txt') as f:
	s = [int(x) for x in f]
	ans = []
	min_ = min([i for i in s if i % 10 == 4])
	max_ = max([i for i in s if i % 10 == 4])
	summa = max_ + min_
	for i in range(len(s) - 1):
		if s[i] + s[i + 1] < summa:
			ans.append(s[i] + s[i + 1])
print(len(ans), max(ans))