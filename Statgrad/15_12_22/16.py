def f(n):
    if n == 0:
        return 0
    return f(n // 10) + (n % 10)


print(f(100))  # сумма цифр, оказывается

print((1_134_567_009 - 237_567_892) // 10 + 1)


# 89699912
