ans = []
for i in range(1, 1000):
    n = bin(i)[2::]
    n = n.replace('1', '', 1)
    if n.count('1') % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '0'
    if int(n, 2) < 450:
        ans.append(int(n, 2))
print(max(ans))

# 444
