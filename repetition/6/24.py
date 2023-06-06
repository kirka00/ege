with open('files/24.txt') as f:
    s = f.readline()
    k = kmax = 1
    ch = ''
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            k = 1
            ch = ''
        else:
            k += 1
            ch += s[i]
            if k > kmax:
                kmax = k
                maxch = max(ch.count(c) for c in set(ch))
print(maxch)


# 19