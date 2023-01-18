from random import randint

spisok = [randint(1, 100) for _ in range(10)]
k = 1
for i in spisok:
    if i // 5 and spisok.index(i) % 2 != 0:
        k *= i
print(k)
