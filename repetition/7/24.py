with open('files/24.txt') as f:
    s = f.readline().split('E')
    minim = 10 ** 10
    for ch in s:
        if ch.count('B') == 2:
            if ch[ch.index('B') + 1:ch.rindex('B')].count('A') > 5:
                minim = min(minim, len(ch) + 2)
print(minim)
                

# 13