# пробный вариант №1
# 5 задача - ? (https://vopvet.ru/news/muzykalnyj_fragment_byl_ocifrovan_75_sek/2016-10-10-5966)

# task_2
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w <= y) and ((x <= z) == (y <= x)):
                    print(x, y, z, w)

'''
x y z w
0 0 1 0
1 0 1 0
1 1 1 0
'''
#################################################################

# task_4
for i in range(100, 1000):
    s = sorted(str(i))
    if s[0] == '0':
        if s[1] == '0':
            minim = maxim = int(s[2] + '0')
        else:
            minim = int(s[1] + '0')
            maxim = int(s[2] + s[1])
    else:
        minim = int(s[0] + s[1])
        maxim = int(s[2] + s[1])
    if maxim - minim == 60:
        print(i)
        break

# task_10
result_search = []
alph = '0123456789abcdefg'
for x in alph:
    f = int(f'9759{x}', 17) + int(f'3{x}108', 17)
    if f % 11 == 0:
        print(f // 11)
        break
