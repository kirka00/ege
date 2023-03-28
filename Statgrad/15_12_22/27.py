def count3(x):
    k3 = 0
    while x % 3 == 0:
        k3 += 1
        x //= 3
    if k3 > 8:
        k3 = 8
    return k3


with open('files/27-B.txt') as f:
    n = int(f.readline())
    data = [int(x) for x in f]
    d = [[0] * 9 for i in range(4)]
    count = 0
    for i in range(n):
        for j in range(8 - count3(data[i]), 8 + 1):
            count += d[(4 - data[i] % 4) % 4][j]
        d[data[i] % 4][count3(data[i])] += 1
print(count)


# 306 360950279
