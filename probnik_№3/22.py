with open('files/24.txt') as f:
   s = f.readline()
   a = [-1]
   kmax = 0
   for i in range(len(s)):
       if s[i] == '.':
           if len(a) > 5:  # проверка длины списка,в котором хранятся индексы и тогда удаляем первый индекс списка (точка)
               a.pop(0)
           a.append(i)  # добавляем очередной индекс
       # разность между текущим индексом и первым значением индекса, помещенного в список
       kmax = max(i - a[0], kmax)
print(kmax)

# 208

with open('files/24.txt') as f:
    s = f.readline()
    kmax = 0
    a = []
    for i in range(len(s)):
        if s[i] == '.':
            a.append(i)
    for i in range(len(a) - 6):
        kmax = max(kmax, a[i + 6] - a[i] - 1)
print(kmax)
