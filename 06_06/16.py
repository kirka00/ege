s = 3000 * [1]
for n in range(1, 3000):
    if n < 3:
        s[n] = 2
    if n > 2:
        s[n] = 2 * s[n - 2]
    

print(s[2222] // s[2182])


# 1048576