with open(f'files/27_A.txt') as f:
    k, n, data = int(f.readline()), int(f.readline()), [int(i) for i in f]
    max_ = kmax = 10 ** -10
    for i in range(n - k - 1, -1, -1):
        max_ = max(data[i + k], max_)
        kmax = max(kmax, data[i] + max_)
    print(kmax)
    

'''
1219
2090920
'''