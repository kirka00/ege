with open('files/4.txt') as f:
    s = [int(x) for x in f]
    n = []
    for i in range(len(s)):
        if s[i] % 13 == 7 and s[i] % 7 and s[i] % 11:
            n.append(s[i])
print(max(n) - min(n), len(n))