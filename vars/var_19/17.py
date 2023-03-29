with open('files/17.txt') as f:
    s = [int(x) for x in f]
    n = []
    for i in range(len(s) - 1):
        if 100 <= abs(s[i]) + abs(s[i + 1]) <= 700:
            n.append(max(s[i], s[i + 1]))


print(len(n), max(n))


# 11 455 
