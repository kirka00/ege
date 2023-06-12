with open('files/16.txt') as f:
    s = f.readline().split('A')
    kmax = 0
    for i in range(len(s) - 1):
        k = s[i] + 'A' + s[i + 1]
        kmax = max(kmax, len(k))
print(kmax)