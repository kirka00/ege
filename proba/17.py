with open('files/17.txt') as f:
    s = [int(x) for x in f]
    ans = []
    min_ = min([q for q in s if 100 <= q <= 999 and q % 10 == 5])
    for i in range(len(s) - 1):
        if (100 <= s[i] <= 999 or 100 <= s[i + 1] <= 999) and \
            ((s[i] + s[i + 1]) % min_ == 0):
            ans.append(s[i] + s[i + 1])
print(len(ans), max(ans))
    

# 13 9500