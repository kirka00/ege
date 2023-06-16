with open("files/4.txt") as f:
	n = int(f.readline())
	a = sorted(map(int, f))
ans = []
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0:
            sr = (a[i] + a[j]) // 2
            if a[2499] < sr < a[3750]:
                ans.append(sr)

print(len(ans), min(ans))