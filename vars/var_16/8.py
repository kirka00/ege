from itertools import product


words = product('1234', repeat=3)
k = set()
for word in words:
    i = ''.join(word)
    if i.count('2') == 1:
        k.add(i)
print(len(k))


# 27
