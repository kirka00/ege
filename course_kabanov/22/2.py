with open('files/2.txt') as f:
    s = f.readline()
    k = 0
    for i in range(len(s)):
        if (s[i] == 'T' and s[i + 1] == 'I' and s[i + 2] == 'K') or \
            (s[i] == 'T' and s[i + 1] == 'O' and s[i + 2] == 'K'):
            k += 1
print(k)
