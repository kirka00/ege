with open('files/17.txt') as f:
    s = [int(x) for x in f]
    ans = []
    max_ = max([q for q in s if len(str(q)) == 2])
    for i in range(len(s) - 1):
        if (len(str(s[i])) == 2 and len(str(s[i + 1]) != 2)) or \
        	(len(str(s[i])) != 2 and len(str(s[i + 1]) == 2)) and \
                ((s[i] + s[i + 1]) % max_ == 0):
            ans.append(s[i] + s[i + 1])
print(len(ans), max(ans))
