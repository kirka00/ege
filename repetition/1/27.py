with open('files/27v16_b.txt') as f:
    n = int(f.readline())
    summa, dmin = 0, 10 ** 10
    for i in range(n):
        a, b = map(int, f.readline().split())
        summa += max(a, b)
        d = abs(a - b)
        if d % 45:
            dmin = min(dmin, d)
    if summa % 45 != 0:
        print(summa)
    else:
        print(summa - dmin)


# 694741 664750894