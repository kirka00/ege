with open('17var02.txt') as f:
    s = [int(x) for x in f]
    n = []
    max_ = max([j for j in s if j % 2 == 0])
    for i in range(len(s) - 1):
        if s[i] + s[i + 1] == max_:
            n.append(s[i] ** 2 + s[i + 1] ** 2)


print(len(n), max(n))
# 4 9994000936 - true
