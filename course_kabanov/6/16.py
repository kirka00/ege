p = list(range(2, 21, 2))
q = list(range(5, 51, 5))
a = list(range(1, 101))
for x in range(1, 101):
	if not (((x in a) <= (x in p)) and ((x in q) <= (x not in a))):
		a.remove(x)
print(a)