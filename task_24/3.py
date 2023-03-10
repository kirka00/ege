'''
Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего не более 106 символов. Определите максимальное количество идущих подряд символов, среди которых нет букв Y, а количество точек не превышает 5.
'''

# вопросы по поводу решения

with open('files/24-181.txt') as f:
   s = f.readline()
   a = [-1]  # индексы последних 7 гласных
   kmax = 0
   for i in range(len(s)):
       if s[i] == 'Y':
           a = [i]
       if s[i] == '.':
           if len(a) > 5:  # проверка длины списка,в котором хранятся индексы и тогда удаляем первый индекс списка (точка)
               a.pop(0)
           a.append(i)  # добавляем очередной индекс
       # разность между текущим индексом и первым значением индекса, помещенного в список
       kmax = max(i - a[0], kmax)
print(kmax)

# 208
