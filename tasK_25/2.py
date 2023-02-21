def f(x):
	ans = set()
	for d in range(1, round(x ** 0.5) + 1):
		if x % d == 0:
			ans.add(d)
			ans.add(x // d)
	return sorted(ans)

max_ans = []
for i in range(394441, 394506):
	if len(f(i)) > len(max_ans):
		max_ans = f(i)
print(len(max_ans), max_ans[-2])


# 48 197225
