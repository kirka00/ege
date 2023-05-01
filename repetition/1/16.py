def f(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        if n % 2 == 0:
            return 3 + f(n - 1)
        else:
            return 2 * n + f(n - 2)
    
print(f(42))

# 884