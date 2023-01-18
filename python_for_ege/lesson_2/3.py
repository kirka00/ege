import math

a, ans = int(input('Введите целое число: ')), []

while a > 0:
    if a % 2 != 0:
        ans.append(int(str(a)[-1]))
    a //= 10


print("кол-во нечётных чисел", len(ans))
print('Их произведение: ', math.prod(ans))
