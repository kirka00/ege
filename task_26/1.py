with open('files/26-5.txt') as f:
    s = int(f.readline().split()[0])
    data = sorted([int(i) for i in f])
    summa = 0
    for count in range(0, len(data)):
        if summa + data[count] > s:
            break
        summa += data[count]
    print(count)
    for i in range(0, len(data)):
        if data[i] - data[count - 1] <= s - summa:
            itog = data[i]
    print(itog)
