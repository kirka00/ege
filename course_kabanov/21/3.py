with open('files/3.txt') as f:
    s = f.readline().replace('D', '*')
    kmax = 0
    for i in s.split('*'):
        kmax = max(kmax, len(i))
print(kmax)