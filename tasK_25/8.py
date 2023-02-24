ans = []
for m in range(1, 1000, 2):
    for n in range(0, 1000, 2):
        if 100_000_000 <= 2 ** m * 7 ** n <= 300_000_000:
            ans.append((2 ** m * 5 ** n, m + n))


for q in sorted(ans):
    print(q[0], q[1])


'''
12500000 13
32000000 17
52428800 23
134217728 27
'''
