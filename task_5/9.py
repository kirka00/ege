for n in range(2, 1000):
    s = bin(n)[2:]
    s += s[-2]
    s += s[1]
    if int(s, 2) > 100:
        print(n)
        break
