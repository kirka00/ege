with open('files/17.txt') as f:
    s = f.readline().split('D')
    kmax = 0
    for i in range(len(s) - 2):
        k = s[i] + 'D' + s[i + 1] + 'D' + s[i + 2]
        kmax = max(kmax, len(k))
print(kmax)