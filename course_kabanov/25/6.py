with open("files/6.txt") as f: 
	n = int(f.readline())
	a = sorted(map(int, f))
k = kmax = 1
for i in range(len(a) - 1):
	if a[i] == a[i + 1]:
		k += 1
		kmax = max(kmax, k)
	else:
		k = 1


print(len(set(a)), kmax)