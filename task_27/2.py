with open('files/dz_2/a.txt') as f:
    n = int(f.readline())
    summa, dmin = 0, 10 ** 10
    for i in range(n):
        a, b = map(int, f.readline().split())
        summa += min(a, b)
        d = abs(a - b)
        if d % 3 != 0:
            dmin = min(dmin, d)
    if summa % 3 != 0:
        print(summa)
    else:
        print(summa + dmin)


# 67303 200157496
