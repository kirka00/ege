b = set(range(160, 181))
def f(x):
	return (x in b) <= ((x % 35 == 0) <= (x % a == 0))


k = set()
for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		k.add(a)
print(len(k))


