for n in range(1000):
    r = bin(n)[2:]
    q = ''
    for w in r:
        if w == '0':
            q += '00'
        else:
            q += '11'
    if int(q, 2) > 63:
        print(int(q, 2))
        break

# 192