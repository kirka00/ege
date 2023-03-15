with open('files/dz_2/b.txt') as f:
    n = int(f.readline())
    summa, dmax = 0, 0
    for i in range(n):
        a, b = map(int, f.readline().split())
        summa += min(a, b)
        d = abs(a - b)
        if d % 3 != 0:
            dmax = max(dmax, d)
    if summa % 3 != 0:
        print(summa)
    else:
        print(summa - dmax)


# 67089 200157480
