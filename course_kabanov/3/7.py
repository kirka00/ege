from itertools import product, permutations



wrong = [''.join(x) for x in product('аиоу', repeat=2)] + [''.join(x) for x in product('бклн', repeat=2)]

k = 0
for i in permutations('абиколун'):
    w = ''.join(i)
    if all(s not in w for s in wrong):
        k += 1
print(k)


# 1152