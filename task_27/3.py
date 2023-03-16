with open('files/dz_3/a.txt') as f:
    n = int(f.readline())
    summa = 0
    d1, d2, d3, d4 = [], [], [], []
    for i in range(n):
        a, b = map(int, f.readline().split())
        summa += min(a, b)
        d = abs(a - b)
        if d % 5 == 1:
            d1.append(d)
        if d % 5 == 2:
            d2.append(d)
        if d % 5 == 3:
            d3.append(d)
        if d % 5 == 4:
            d4.append(d)
    print(summa % 5)
    print(summa - min(d4))
    print(summa - (min(d1) + min(d3)))


# 73878 203343854
