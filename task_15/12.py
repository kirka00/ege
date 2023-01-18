p = set(range(1, 7))
q = set([3, 5, 15])
a = set()
for x in range(-1000, 1000):
	if not ((x not in a) <= ((x not in p) and (x in q)) or (x not in q)):
		a.add(x)
print(a)
print(len(a))
