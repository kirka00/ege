s = 33 * '9992' + 14 * '2' + '29' + 14 * '1'  # правильное расположение цифр
while '999' in s or '22' in s:
    if '999' in s:
        s = s.replace('999', '12')
    else:
        s = s.replace('22', '1')
        
print(s.count('1'))