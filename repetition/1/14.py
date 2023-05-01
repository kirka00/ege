for x in range(26):
    flag = True
    for y in range(26):
        d1 = 26 ** 4 + 3 * 26 ** 3 + y * 26 ** 2 + x * 26 + 5
        d2 = 2 * 26 ** 4 + 4 * 26 ** 3 + y * 26 ** 2 + 26 + 3
        if (d1 + d2) % 8:
            flag = False
            break
    if flag:
        res = x
d1 = 26 ** 4 + 3 * 26 ** 3 + 2 * 26 ** 2 + x * 26 + 5
d2 = 2 * 26 ** 4 + 4 * 26 ** 3 + 2 * 26 ** 2 + 26 + 3

print((d1 + d2) // 8)

# 187168