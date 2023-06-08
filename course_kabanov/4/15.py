for x in range(21, 29):
    q = ''
    w = x
    while w > 0:
        q += str(w % 3)
        w //= 3
    if q[-3:-1] == '11':
        print(x)
        