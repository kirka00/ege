with open('files/27-B.txt') as f:
    n = int(f.readline())
    count = summa = 0
    count_ost = [1] + [0] * 998
    for i in range(n):
        summa += int(f.readline())
        ostat = summa % 999
        count += count_ost[ostat]
        count_ost[ostat] += 1
print(count)
    

'''
403
1801801220
'''