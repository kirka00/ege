from itertools import product

words = product('12345', repeat=4)
k = 0
for word in words:
    i = ''.join(word)
    if i.count('5') == 1:
        k += 1
print(k)


# 256 - true
