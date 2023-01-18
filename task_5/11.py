k = 0
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '11'
    else:
        s = '11' + s + '0'
    if 500 <= int(s, 2) <= 1000:
        k += 1
print(k)
