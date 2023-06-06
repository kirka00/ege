with open('files/24.txt') as f:
    s = f.readline()
    k = kmax = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            k += 1
            kmax = max(kmax, k)
        else:
            k = 0
print(kmax)


# 6