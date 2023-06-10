with open('files/17.txt') as f:
	s = [int(x) for x in f]
	ans = []
	maxim = max(x for x in s if all(i in '13579' for i in str(x)))
	for i in range(len(s) - 1):
		if (all(x in '02468' for x in str(s[i])) or all(x in '02468' for x in str(s[i + 1]))):
			if s[i] + s[i + 1] > maxim:
				ans.append(s[i] + s[i + 1])
print(len(ans), max(ans))
	  
# 56 18612