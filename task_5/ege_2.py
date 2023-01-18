for i in range(2, 1000):
    s = bin(i)[2:]
    s += s[-2]
    s += s[1]
    if int(s, 2) > 170:
        print(i)
        break


k = set()
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '10'
    else:
        s = '11' + s + '0'
    if 800 <= int(s, 2) <= 1500:
        k.add(s)
print(len(k))



for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + s + '1'
    else:
        s = '1' + s + '01'
    if int(s, 2) > 420:
        print(n)
        break
