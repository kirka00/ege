stroka = input().lower()
a, b, c = stroka.count('е'), stroka.count('г'), stroka.count('э')
if a > 0:
    print(f'''Буква 'е' встречается {a} раз''')
if b > 0:
    print(f'''Буква 'г' встречается {b} раз''')
if c > 0:
    print(f'''Буква 'э' встречается {c} раз''')
if a == 0 and b == 0 and c == 0:
    print('''В введенном предложении нет букв 'е', ' г ', 'э'.''')
