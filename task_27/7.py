'''with open('files/dz_7/a.txt') as f:
    n = int(f.readline())
    s = [int(i) for i in f]
    count = 0
    for i in range(n):
        peoizv = 1
        for j in range(i, n):
            peoizv *= s[j]
            if peoizv % 524288 != 0:
                count += 1
print(count)'''


def prost(a):
    for d in range(2, int(a ** 0.5) + 1):
        if a % d == 0:
            return False
    return True


divs = []
for i in range(2, int(524288 ** 0.5) + 1):
    if 524288 % i == 0 and prost(i):
        divs.append(i)
print(divs)  # [2]

with open('files/dz_7/a.txt') as f:
    n = int(f.readline())
    count = k = 0
    data = [int(i) for i in f]
    dic = {2: 0}
    for i in data:
        k += 1
        for d1, d2 in dic.items():
            if i % d1 == 0:
                dic[d1] = k
        count += k - min(dic.values())
print(count)


# 1118 206138
