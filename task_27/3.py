with open('files/dz_3/b.txt') as f:
    n = int(f.readline())
    D = 5
    s, dmin = 0, [10 ** 10] * D
    for i in range(n):
        a, b = map(int, f.readline().split())
        s += min(a, b)
        d = abs(a - b)
        r = d % D
        if r > 0:
            dminnov = dmin[:]
            for k in range(1, D):
                r0 = (r + k) % D
                dminnov[r0] = min(d + dmin[k], dminnov[r0])
            dminnov[r] = min(d, dminnov[r])
            dmin = dminnov[:]
        if s % D == 0:
            print(s)
        else:
            print(s, s % D)
            print(dmin)
            print(s + dmin[D - s % D])



# 75960 203343860
