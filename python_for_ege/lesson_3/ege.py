stroka = 'hello'
for i in stroka:
    print(i)

for i in range(4, 40, 4):
    print(i)

# break and continue

a = 0
for i in range(2, 51, 2):
    a += i
print(a)

print(type(int('123')))

# конкатенация
print('123' + '456')

print('hello\n' * 15)

# индексы и срезы
print(stroka[::-1])

# строковые методы
print(stroka.isdigit())  # все цифры
print(stroka.isalpha())  # все буквы
print('-'.join(stroka))  # h-e-l-l-o
print(stroka.find('l'))  # найти индекс элемента слева
print(stroka.rfind('l'))  # найти индекс элемента справа
print(stroka.count('l'))  # кол-во символов в строке
print(stroka.replace('l', '0'))  # замена символов
print(stroka.replace('l', '0', 1))  # замена 1го символа
print(ord('f'))  #  код символа
print(chr(102))  #  символ по коду




a = 'hello bye'
print(a.split())
