from itertools import product

k = 0
for i in product('видео', repeat=6):
    w = ''.join(i)
    glas = [i for i in w if i in 'иео']
    if w.count('и') >= 1 and w.count('е') >= 1 and glas == sorted(glas):
        k += 1
print(k)


# 1215