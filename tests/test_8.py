import sys


d = list(range(17, 59))
c = list(range(29, 81))
a = []
for x in range(1, 500):
    if not ((x in d) <= (((x not in c) and (x not in a)) <= (x not in d))):
        a.append(x)
print(len(a))

sys.setrecursionlimit(20_000)
def f(n):
	if n >= 2025:
		return n
	if n < 2025:
		return n + f(n  + 2)
print(f(2022) - f(2023))

