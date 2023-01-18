from functools import lru_cache


@lru_cache
def f(x, y, command):
	if x > y or x == 25 or x == 30:
		return 0
	elif x == y:
		return 1
	k = f(x + 1, y, 0)
	k += f(x + 2, y, 0) if x != 14 else 0
	k += f(x * 3, y, 1) if command != 1 and not(6 <= x <= 14) else 0
	return k

print(f(1, 43, 0))


# 36253635
