with open('files/k7a-2.txt') as f:
    s = f.readline()
    k = kmax = 0
    for i in range(len(s)):
        if s[i] in 'ACD':
            k += 1
            kmax = max(kmax, k)
        else:
            k = 0
print(kmax)

# 11
