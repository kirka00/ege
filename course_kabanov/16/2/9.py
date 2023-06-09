s = [1] * 10_000
for n in range(len(s)):
    if n == 1:
        s[n] = 2
    if n > 1:
        s[n] = 2 * s[n - 1]
        

print(s[1900] // (2 ** 1890))