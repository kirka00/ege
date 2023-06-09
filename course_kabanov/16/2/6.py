s = [1] * 25_000
for n in range(len(s)):
    if n == 1:
        s[n] = n
    if n > 1:
        s[n] = (2 * n - 1) * s[n - 1]


print(s[3516] // s[3513])