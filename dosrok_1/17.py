with open('files/17.txt') as f:
	s = [int(x) for x in f]
	ans = []
	min_ = min([x for x in s if 100 <= x <= 999 and x % 10 == 5])
	for i in range(len(s) - 1):
		if ((len(str(s[i])) == 3 and len(str(s[i + 1])) != 3) or (len(str(s[i])) != 3 and len(str(s[i + 1])) == 3)) and ((s[i] + s[i + 1]) % min_ == 0):
			ans.append(s[i] + s[i + 1])
print(len(ans), min(ans))


# 2 33120
