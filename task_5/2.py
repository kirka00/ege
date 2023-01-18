k = 0
for i in range(500, 601):
    s = sorted(str(i))
    if s[0] == '0':
        if s[1] == '0':
            minim = maxim = int(s[2] + '0')
        else:
            minim = int(s[1] + '0')
            maxim = int(s[2] + s[1])
    else:
        minim = int(s[0] + s[1])
        maxim = int(s[2] + s[1])
    if maxim - minim == 10:
        k += 1
print(k)
