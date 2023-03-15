with open('files/4/27-4b.txt') as f:
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
    print(summa - max(d4))
    print(summa - (max(d1) + max(d3)))


# 69446 203334056
