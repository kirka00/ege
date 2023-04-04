with open('files/1.txt') as f:
    s = f.readline()
    k = 0
    for i in range(len(s)):
        if s[i] == 'X' and s[i + 1] == 'V' and s[i + 2] == 'I' \
        and s[i + 3] == 'I' and s[i + 4] == 'I':
            k += 1
print(k)
