p = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
q = set([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
a = set(range(-1000, 1000))
for x in range(-1000, 1000):
	if not (((x in a) <= (x in p)) and ((x in q) <= (x not in a))):
		a.remove(x)
print(a)
print(len(a))
