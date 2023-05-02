with open('files/24var14-20.txt') as f:
    s = f.readline()
    k = kmax = 1
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            k += 1
            kmax = max(k, kmax)
        else:
            k = 1
print(kmax)

# 8