k = 0
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '11'
    else:
        s = '11' + s + '0'
    if int(s, 2) in range(500, 1001):
        k += 1
print(k)


# 59