s = [1] * 25000
for n in range(len(s)):
    if n == 1:
        s[n] = 1
    if n > 1:
        s[n] = n ** 2 + s[n - 1]
    
print(s[1000] - s[997])