for n in range(1, 256):
    s = bin(n)[2:]
    s = (8 - len(s)) * '0' + s
    s1 = ''
    i = s.rindex('1')
    for x in range(i):
        if s[x] == '1':
            s1 += '0'
        else:
            s1 += '1'
    s1 += s[i:]
    if int(s1, 2) == 11:
        print(n)
