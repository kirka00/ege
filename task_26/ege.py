with open('files/26-89.txt') as f:
	n = int(f.readline())
	data = sorted([int(i) for i in f], reverse=True)
	k, box = 1, data[0]
	for i in range(1, len(data)):
		if box - data[i] >= 3:
			k += 1
			box = data[i]
print(k, box)


'''
331 10
'''
