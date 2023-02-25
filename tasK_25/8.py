ans = []
for m in range(0, 1000, 2):
    for n in range(1, 1000, 2):
        if 100_000_000 <= 2 ** m * 5 ** n <= 300_000_000:
            ans.append((2 ** m * 5 ** n, m + n))


for q in sorted(ans):
    print(q[0], q[1])


'''
125000000 15
131072000 23
195312500 13
204800000 21
'''
