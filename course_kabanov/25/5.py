with open("files/5.txt") as f:
	n = int(f.readline())
	a = sorted(map(int, f))
d = set(a)
ans = []
for i in range(n):
    for j in range(i + 1, n):
        if a[i] % 2 != a[j] % 2 and a[i] + a[j] in d:
                ans.append(a[i] + a[j])

print(len(ans), max(ans))