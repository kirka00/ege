import sys


sys.setrecursionlimit(20000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * n + f(n - 1)


print(f(2023) - f(2019))


# 16345854 - true
