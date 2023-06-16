with open("files/7.txt") as f: 
	n = int(f.readline())
	a = [0] * 2_000_001
	for i in range(n):
		start, end = map(int, f.readline().split())
		a[start] += i
		a[end] -= i

k = 0
start, end = -1, 0
count, length = 0, 0
for i in range(2_000_001):
	k0 = k
	k += a[i]
	if k > 0 and start == -1: start = i
	if k == 0 and k0 > 0:
		end = i
		count += 1
		length += end - start
		start, end = -1, 0
print(count, length)


# 1226 822055