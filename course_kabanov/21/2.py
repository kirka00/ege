with open('files/2.txt') as f:
    s = f.readline().replace('A', '*').replace('B', '*').replace('E', '*').replace('F', '*')
    k = kmax = 0
    for i in s:
        if i == '*':
            k += 1
            kmax = max(kmax, k)
        else:
            k = 0
print(kmax)