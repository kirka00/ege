p = set(range(20, 30))
q = set(range(5, 15))
r = set(range(35, 50))
a = set()
for x in range(-1000, 1000):
	if not (((x in p) <= (x in q)) or ((x not in a) <= (x in r))):
		a.add(x)
print(a)
print(len(a))
