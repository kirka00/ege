from itertools import product

words = product('123456', repeat=5)
k = 0
for word in words:
    i = ''.join(word)
    if i.count('1') == 1:
        k += 1
print(k)


# 3125
