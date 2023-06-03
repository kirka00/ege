def f(x):
    return (x & 103 == 0) and (x & 94) <= (x & a)


for a in range(100000):
	if all(f(x) for x in range(100000)):
		print(a)
		break