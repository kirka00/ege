with open('files/2.txt') as f:
    s = [int(x) for x in f]
    n = []
    for i in range(len(s)):
        if (str(s[i])[-1] == '2' or str(s[i])[-1] == '7') \
            and s[i] % 3 == 0 and s[i] % 11 == 0:
            n.append(s[i])
print(len(n), min(n))