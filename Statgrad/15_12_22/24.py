# I способ
with open('files/24.txt') as f:
    s = f.readline().split('F')
    k, kmax = 1, 1
    for i in range(1, len(s)):
        if s[i].count('A') <= 2:
            k += len(s[i]) + 1
            kmax = max(kmax, k)
        else:
            k = 1
print(kmax)


# 266

# II способ
with open('files/24.txt') as f:
    s = f.readline().split('F')[1:-1]
    kmax, chain = 1, 'F'
    for i in s:
        if i.count('A') <= 2:
            chain += i + 'F'
            kmax = max(kmax, len(chain))
        else:
            chain = 'F'
print(kmax)
