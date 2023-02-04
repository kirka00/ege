for i in range(1000):
    n = bin(i)[2:]
    if n[-1] == 0:
        n += '0'
    else:
        n += '1'
    if n.count('1') % 3 == 0:
        n = '11' + n[2:]
    else:
        n = '10' + n[2:]
    if int(n, 2) >= 26:
        print(i)
        break
# true
