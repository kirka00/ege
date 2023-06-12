with open('files/1.txt') as f:
    s = f.readline()
    k = kmax = 0
    for i in s:
        if i == 'C':
            k += 1
            kmax = max(kmax, k)
        else:
            k = 0
print(kmax)