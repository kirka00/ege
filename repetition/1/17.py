with open('files/17var16.txt') as f:
    s = [int(x) for x in f]
    ans = []
    for i in range(len(s) - 1):
        if s[i] > 300 or s[i + 1] > 300:
            ans.append(s[i] ** 2 + s[i + 1] ** 2)
print(len(ans), min(ans))


# 4024 176285