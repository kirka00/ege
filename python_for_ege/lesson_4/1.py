stroka = [i for i in input()]
while 'е' in stroka or 'г' in stroka or 'э' in stroka:
    stroka.remove('е')
    stroka.remove('г')
    stroka.remove('э')
print(stroka)
