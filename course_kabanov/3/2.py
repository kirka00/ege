from itertools import product


k = set()
for i in product('abcwxyz', repeat=6):
    w = ''.join(i)
    if w[0] in 'wxyz' and w[-1] in 'wxyz' and \
        'w' not in w[1:-1] and 'x' not in w[1:-1] and \
            'y' not in w[1:-1] and 'z' not in w[1:-1]:
        k.add(w)
        
print(len(k))


# 1296