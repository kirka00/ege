with open('files/27a.txt') as f:
	n = int(f.readline())
	k = int(f.readline())
	data = [int(i) for i in f]
	minim = 10 ** 10
	for i in range(n - k):
		for j in range(i + k, n):
			if data[i] * data[j] % 157 == 0:
				minim = min(minim, data[i] * data[j])
print(minim)
# 2958822 - 27A
# 75360 - 27B

# B
with open('files/27b.txt') as f:
	n = int(f.readline())
	k = int(f.readline())
	data = [int(i) for i in f]
	mn = m = m157 = 10 ** 10
	for i in range(k, n):
		if data[i - k] % 157 == 0:
			m157 = min(m157, data[i - k])
		else:
			m = min(m, data[i - k])
		if data[i] % 157 == 0:
			mn = min(mn, data[i] * m, data[i] * m157)
		else:
			mn = min(mn, data[i] * m157)
print(mn)

