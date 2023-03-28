from itertools import product

words = product('abs', repeat=6)
k = 0
for i in words:
    print(i)
    word = ''.join(i)
    if word.count('a') == 1:
        k += 1
print(k)


# 192
