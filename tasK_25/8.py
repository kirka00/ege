ans = []
for m in range(0, 1000, 2):
    for n in range(1, 1000, 2):
        if 100_000_000 <= 2 ** m * 7 ** n <= 300_000_000:
            ans.append((2 ** m * 5 ** n, m + n))


for q in sorted(ans):
    print(q[0], q[1])


'''
7812500 11
20000000 15
51200000 19
83886080 25
'''
