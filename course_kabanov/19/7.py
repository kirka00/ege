def f(x, y, z, p):
	if x + y + z >= 73 or p > 2:
		return p == 2

	return f(x + 3, y, z, p + 1) or f(x, y + 3, z, p + 1) or f(x, y, z + 3, p + 1) or\
	f(x + 13, y, z, p + 1) or f(x, y + 13, z, p + 1) or f(x, y, z + 13, p + 1) or \
	f(x + 23, y, z, p + 1) or f(x, y + 23, z, p + 1) or f(x, y, z + 23, p + 1) 
    

print(min([i for i in range(24)  if f(2, i, 2 * i, 0)]))


def f(x, y, z, p):
	if x + y + z >= 73 or p > 3:
		return p == 3
	if p % 2:
		return f(x + 3, y, z, p + 1) and f(x, y + 3, z, p + 1) and f(x, y, z + 3, p + 1) and\
		f(x + 13, y, z, p + 1) and f(x, y + 13, z, p + 1) and f(x, y, z + 13, p + 1) and \
		f(x + 23, y, z, p + 1) and f(x, y + 23, z, p + 1) and f(x, y, z + 23, p + 1) 
	else:
		return f(x + 3, y, z, p + 1) or f(x, y + 3, z, p + 1) or f(x, y, z + 3, p + 1) or\
		f(x + 13, y, z, p + 1) or f(x, y + 13, z, p + 1) or f(x, y, z + 13, p + 1) or \
		f(x + 23, y, z, p + 1) or f(x, y + 23, z, p + 1) or f(x, y, z + 23, p + 1) 
    

print(([i for i in range(24)  if f(2, i, 2 * i, 0)]))


def f(x, y, z, p):
	if x + y + z >= 73 or p > 4:
		return p == 2 or p == 4
	if p % 2:
		return f(x + 3, y, z, p + 1) and f(x, y + 3, z, p + 1) and f(x, y, z + 3, p + 1) and\
		f(x + 13, y, z, p + 1) and f(x, y + 13, z, p + 1) and f(x, y, z + 13, p + 1) and \
		f(x + 23, y, z, p + 1) and f(x, y + 23, z, p + 1) and f(x, y, z + 23, p + 1) 
	else:
		return f(x + 3, y, z, p + 1) or f(x, y + 3, z, p + 1) or f(x, y, z + 3, p + 1) or\
		f(x + 13, y, z, p + 1) or f(x, y + 13, z, p + 1) or f(x, y, z + 13, p + 1) or \
		f(x + 23, y, z, p + 1) or f(x, y + 23, z, p + 1) or f(x, y, z + 23, p + 1) 
    

print(([i for i in range(24)  if f(2, i, 2 * i, 0)]))