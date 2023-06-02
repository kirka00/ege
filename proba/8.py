from itertools import product

k = 0
for i in product('аворт', repeat=6):
    w = ''.join(i)
    k += 1
    if w == 'ворота':
        print(k)
        break


# 4821