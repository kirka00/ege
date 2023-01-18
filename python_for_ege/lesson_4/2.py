from random import randint

spisok = [randint(1, 10) for _ in range(10)]
for i in spisok:
    if i < 3:
        spisok.remove(i)
print(sum(spisok) / len(spisok))
