def d(a):
    b = ''
    s = 0
    while a != 0:
        b = str(a % 9) + b
        s += a % 9
        a = a // 9
    return b, s


for i in range(0, 10):  # ?
    for j in range(0, 9999):  # *
        x = f'3{i}458{j}3'
        c = d(int(x))[0]
        s = 1
        for z in range(len(c) - 1):
            if c[z] < c[z + 1]:
                s = 0
                break
        if s == 1:
            print(x, d(int(x))[1])


'''
39458583 15
39458673 17
'''
