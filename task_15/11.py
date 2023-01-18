p = set(range(25, 50))
q = set(range(40, 75))
a = set()
for x in range(-1000, 1000):
	if not (x in q) <= (((x in p) == (x in q)) or ((x not in p) <= (x in a))):
		a.add(x)
print(a)
print(len(a))
