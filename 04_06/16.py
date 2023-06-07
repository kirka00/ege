s = 3000 * [1]
for n in range(len(s), 1, -1):
    if n < 2222:
        s[n] = n ** 3 + s[n + 2]

print(s[4] - s[10])


# 792