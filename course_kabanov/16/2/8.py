from functools import lru_cache


@lru_cache
def f(n):
    if n > 100:
        return n - 10_000
    if 1 <= n <= 10_000:
        return f(n + 1)	+ f(n + 2)
    

print(f(12345) * ((f(10) - f(12)) // f(11)) + f(10_101))