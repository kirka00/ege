from random import randint

set_1 = {randint(0, 20) for _ in range(20)}
set_2 = {randint(50, 70) for _ in range(20)}
print(set_1 | set_2)
print(set_1.difference(set_2))
print(set_1 & set_2)  # нет пересечения
