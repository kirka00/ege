from itertools import permutations


words = permutations('спортлото')
k = set()
for i in words:
    w = ''.join(i)
    if 'тт' in w:
        k.add(w)
print(len(k))


# 6720