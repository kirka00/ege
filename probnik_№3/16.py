def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    if n >= 2 and n % 2:
        return f(n - 3) + 3


n = 0
while f(n) != 31:
    n += 1
print(n)


# 893
