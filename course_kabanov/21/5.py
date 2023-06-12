with open('files/5.txt') as f:
    s = f.readline().replace('A', '*').replace('B', '*').replace('C', '*')
    kmax = 0
    for i in s.split('*'):
        kmax = max(kmax, len(i))
print(kmax)