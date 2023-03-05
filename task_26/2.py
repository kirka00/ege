with open('files/26-k4.txt') as f:
	n, k = map(int, f.readline().split())
	print(k)
	data = sorted([int(i) for i in f], reverse=True)
	print(sum(data[k:k+k]) // k, sum(data[:k]) // k)



'''
856 953
'''
