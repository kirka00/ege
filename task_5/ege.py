k = set()
for i in range(1, 1000):
    s = bin(i)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if 210 <= int(s, 2) <= 260:
        k.add(int(s, 2))
print(len(k))
