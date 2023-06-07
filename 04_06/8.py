from itertools import product

q = []
for i in product('аклмня', repeat=5):
    w = ''.join(i)
    if 'мн' == w[0:2]:
        q.append(w)
print(len(q) - 2)