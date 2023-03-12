p = set(range(15, 31))
q = set(range(5, 61))
a = set()
for x in range(-1000, 1000):
	if not (not ((x in q)) or (x in p) and (x in a)):
		a.add(x)
print(a)
print(len(a))



# 55
