with open('files/26.txt') as f:
    k, n, data = int(f.readline()), int(f.readline()), []
    for i in range(n):
        a1, b1 = map(int, f.readline().split())
        data.append([a1, b1])
    data.sort()
    sp = [[0, 0]] * k
    for i in range(k):
        sp[i] = data[i]
    count = k
    for x in range(k, len(data)):
        for i in range(len(sp)):
            if data[x][0] > sp[i][1] and data[x][1] <= 24 * 60:
                sp[i] = data[x]
                t = i + 1
                count += 1
                break
    print(count, t)
# 389 133