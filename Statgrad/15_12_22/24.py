with open('files/24.txt') as f:
    s = f.readline().split('F')
    k, kmax = 1, 1
    for i in range(1, len(s)):
        if s[i].count('A') <= 2:
            k += len(s[i]) + 1
            kmax = max(kmax, k)
        else:
            k = 1
print(kmax)


# 266
