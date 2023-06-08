from itertools import product

k = 0
for i in product('кресло', repeat=4):
    w = ''.join(i)
    if w[0] in 'крсл' and w[-1] in 'ео':
        k += 1
        
print(k)


# 288