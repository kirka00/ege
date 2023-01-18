def f(x, y):  # 6
    if x < y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x - 3, y) + f(x // 7, y)


print(f(50, 1))


print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if w and ((x <= y) == (y <= z)):
                    print(w, x, y, z)

def f(n):
    if n <= 10:
        return n
    elif n >= 10:
        return 1
    elif 10 < n < 10000 and n % 2 == 0:
        return n % 10 + f(n + 2)
    elif 10 < n < 10000 and n % 2 != 0:
        return f(n - 2) - (n - 1) ^ 10



print(f(4500) + f(5515))


def f(n, m):
	return (n % m == 0)

def x(s, d):
        return s + d > 0

for a in range(1, 1000):
	if all(f((n, m) for x in range(1, 1000)):
		print(a)
		break
