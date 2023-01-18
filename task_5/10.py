for n in range(101, 1000):
    s = bin(n)[2:]
    for i in range(3):
        if s.count('1') == s.count('0'):
            s += s[-1]
        elif s.count('1') > s.count('0'):
            s += '0'
        else:
            s += '1'
    if int(s, 2) % 4 == 0 and int(s, 2) % 8 != 0:
        print(n)
        break
