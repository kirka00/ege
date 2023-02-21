def prost(x):
	ans = set()
	for d in range(2, round(x ** 0.5) + 1):
		if x % d == 0:
			return False
	return True


k = []
for i in range(125697, 190235):
	for d in range(2, round(i ** 0.5)):
		if d * (i // d) == i and prost(d) and prost(i // d):
			k.append(i)

print(len(k), max(k))


# 14047 190231
