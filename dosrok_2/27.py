with open('files/27-b.txt') as f:
	k = int(f.readline())
	n = int(f.readline())
	data  = [int(x) for x in f]
	ms = m = 0
	for i in range(k ,n):
		m = max(m, data[i - k])
		ms = max(ms, data[i] + m)
print(ms)


# 19974 18469835
