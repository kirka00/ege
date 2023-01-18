a = '4' * 9 + '5' * 12
while '444' in a or '888' in a:
    if '444' in a:
        a = a.replace('444', '8', 1)
    while '555' in a:
        a = a.replace('555', '8', 1)
    while '888' in a:
        a = a.replace('888', '3', 1)
print(a)
