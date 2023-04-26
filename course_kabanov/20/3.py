with open('files/3.txt') as f:
    s = [int(x) for x in f]
    n = []
    for i in range(len(s)):
        if (str(s[i])[-1] == '5' or str(s[i])[-1] == '7') \
            and s[i] % 9 and s[i] % 11:
            n.append(s[i])
print(len(n), max(n) + min(n))