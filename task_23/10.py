import math

def f(x, y):
	if x > y or x == 12:
		return 0
	elif x == y:
		return 1
	return f(x + 1, y) + f(x + 4, y) + f(math.factorial(x + 1), y)


print(f(2, 24))
