with open('files/4.txt') as f:
    s = f.readline().replace('C', '*').replace('F', '*')
    kmax = 0
    for i in s.split('*'):
        kmax = max(kmax, len(i))
print(kmax)