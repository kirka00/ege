def f(n):
    if n > 1_000:
        return n
    else:
        return f(n + 1) + 5 * n + 2
    

print(f(3) - f(7))
        