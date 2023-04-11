from itertools import product



k = 0
for i in product('аклмня', repeat=5):
    w = ''.join(i)
    k += 1
    if w[0:2] == 'км':
        print(k)
        break


# 1945
