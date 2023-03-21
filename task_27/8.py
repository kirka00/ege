with open('files/dz_8/b.txt') as f:
	n, v = map(int, f.readline().split())
	data = []
	for x in f:
		number, prob = map(int, x.split())
		if prob % v == 0:
			data.append([number, prob // v])
		else:
			data.append([number, prob // v + 1])
	data.sort()
	min_s = 10 ** 30
	k_do = n * [0]
	k_do[0] = data[0][1]
	for i in range(1, n):
		k_do[i] = k_do[i - 1] + data[i][1]
	stoimost0 = 0
	for i in range(n):
		stoimost0 += abs(data[i][0] - data[0][0]) * data[i][1]
	for i in range(1, n):
		stoimost0 = stoimost0 + (data[i][0] - data[i - 1][0]) * k_do[i - 1] \
				- (data[i][0] - data[i - 1][0]) * (k_do[-1] - k_do[i - 1])
		min_s = min(min_s, stoimost0)
print(min_s)


# 
