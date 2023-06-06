from itertools import permutations

k = 0
for i in permutations('ярослав', r=5):
    w = ''.join(i)
    s = ''
    for q in w:
        if q in 'рслв':
            s += 's'
        else:
            s += 'g'
    if 'gg' not in s and s.count('s') > s.count('g'):
        k += 1
        
print(k)


# 1224