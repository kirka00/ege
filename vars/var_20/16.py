def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2 and n % 2 == 0:
        return (8 * n + f(n - 3)) // 9
    if n > 2 and n % 2:
        return (4 * n + f(n - 1) + f(n - 2)) // 7


print(f(52))


# 50 - true
