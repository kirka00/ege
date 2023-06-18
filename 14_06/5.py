for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '0'
    else:
        r += '1'
    if r.count('1') % 2:
        r += '1'
    else:
        r += '0'
    q = int(r, 2)
    if q >= 2023:
        print(q)
        break
    

# 2025