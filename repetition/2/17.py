with open('files/17.txt') as f:
    s = [int(x) for x in f] 
    ans = []
    max_3 = max([i for i in s if str(abs(i))[-1] == '3'])
    for i in range(len(s) - 1):
        if ((abs(s[i]) % 10 == 3 and abs(s[i + 1]) % 10 != 3) or (abs(s[i + 1]) % 10 == 3 and abs(s[i]) % 10 != 3)) and (s[i] ** 2 + s[i + 1] ** 2) >= max_3 ** 2:
            ans.append(s[i] ** 2 + s[i + 1] ** 2)
            
print(len(ans), max(ans))


# 180 190360573