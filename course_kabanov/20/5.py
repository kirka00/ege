with open('files/5.txt') as f:
    s = [int(x) for x in f]
    n = []
    for i in range(len(s)):
        if hex(s[i])[-1] == 'b' and s[i] % 7 == 0 and s[i] % 6 \
            and s[i] % 13 and s[i] % 19:
            n.append(s[i])
print(sum(n), len(n))