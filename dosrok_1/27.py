with open('files/27-b.txt') as f:
	n = int(f.readline())
	k = int(f.readline())
	data = [int(i) for i in f]
	ms = m = 0
	for i in range(k, n):
		m = max(m, data[i -k])
		ms = max(ms, data[i] + m)
print(ms)


# 174902 3094684
