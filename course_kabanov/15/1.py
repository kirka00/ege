for i in range(1, 1000):
    r = bin(i)[2:]
    r += str(sum([int(i) for i in r]) % 2)
    r += str(sum([int(i) for i in r]) % 2)
    q = int(r, 2)
    if q > 80:
        print(q)
        break
    
    