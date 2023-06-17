with open('files/27A.txt') as f:
    n = int(f.readline())
    k = int(f.readline())
    a = [int(x) for x in f]

m = 0
for i in range(n):
	for j in range(i + 1, n):
		if j - i >= k:
			m = max(m, a[i] + a[j])
print(m)