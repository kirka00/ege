with open('files/6.txt') as f:
    s = f.readline()
    k = kmax = 0
    for i in s:
        if i in '12345677890':
            k += 1
            kmax = max(kmax, k)
        else:
            k = 0
print(kmax)