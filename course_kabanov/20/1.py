with open('files/1.txt') as f:
    s = [int(x) for x in f]
    n = []
    for i in range(len(s)):
        if s[i] % 3 == 0 and s[i] % 7 and s[i] % 17 and s[i] % 19 \
            and s[i] % 27:
            n.append(s[i])
print(len(n), max(n))