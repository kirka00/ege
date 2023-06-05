def f(x, y, k):
	if k == 0:
		k = [0, 0, 0]
	if x > y or k[0] > 4 or k[2] > 5: 
		return 0
	if x == y:
		return 1 if k[1] >= 2 and k[2] == 5 else 0
	return f(x * 5, y, [k[0] + 1, k[1], k[2]]) + f(x * 3, y, [k[0], k[1] + 1, k[2]]) + f(x + 45, y, [k[0], k[1], k[2] + 1])


print(f(1, 2970, 0))


# 74