s = set()


def f(x, k):
	global s
	if k == 6:
		s.add(x)
	else:
		f(x + 1, k + 1)
		f(x + 2, k + 1)
		f(x * 2, k + 1)



f(1, 0)
ans = []
for i in list(s):
	if 34 <= i <= 59:
		ans.append(i)
print(len(ans))
