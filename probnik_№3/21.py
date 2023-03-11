def f(x, y, flag):
    if x == y:
        return 1
    elif x > y:
        return 0
    else:
        return f(x + 1, y, False) + f(x + 3, y, False) if flag \
            else f(x + 1, y, False) + f(x + 3, y, False) + f(x * 2, y, True)


print(f(1, 14, False))


def f(x, y, command):
	if x > y:
		return 0
	elif x == y:
		return 1
	k = f(x + 1, y, 0)
	k += f(x + 3, y, 0)
	k += f(x * 2, y, 1) if command != 1  else 0
	return k


print(f(1, 14, 0))


# 260
