s = set()
def f(x, k):
	global s
	if k == 11:
		s.add(x)
	else:
		f(x + 1, k + 1)
		f(x * 2 + 1, k + 1)


f(3, 0)
print(len(s))
