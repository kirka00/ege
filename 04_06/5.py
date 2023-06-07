for n in range(10, 200):
    r = bin(n)[2:]
    if n % 5 == 0:
        r += r[3:]
    else:
        r += bin((n % 5) * 5)[2:]
    if int(r, 2) > 512:
        print(n)
        break
    
# 19