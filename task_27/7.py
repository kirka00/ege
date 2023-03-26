with open('files/dz_7/a.txt') as f:
    n = int(f.readline())
    s = [int(i) for i in f]
    count = 0
    for i in range(n):
        peoizv = 1
        for j in range(i, n):
            peoizv *= s[j]
            if peoizv % 524288 != 0:
                count += 1
print(count)


with open('files/dz_7/b.txt') as f:
    n = int(f.readline())
    m = 524_288
    k, i, d, ans = {}, 2, {}, 0
    while m > 1:
        while m % i == 0:
            k[i] = k.get(i, 0) + 1
            m //= i
        i += 1
    print(k)
    for i in k:
        d[i] = [0] * k[i]
    for i in range(1, n + 1):
        num = int(f.readline())
        for j in d:
            while num % j == 0:
                d[j].pop(0)
                d[j].append(i)
                num //= j
        ans += i - min(min(d.values()))
print(ans)


# 18871 3921243
