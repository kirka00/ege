x = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
a = []
while x != 0:
    b = x % 15
    if not b in a:
        a.append(b)
    x //= 15
print(len(a))


# 10
