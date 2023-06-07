from functools import lru_cache


@lru_cache()
def f(n):
    if n >= 2222:
        return n
    else:
        n ** 3 + f(n + 2)
        

print(f(4) - f(10))