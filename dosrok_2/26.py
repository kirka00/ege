with open('files/26.txt') as f:
	k = int(f.readline())
	n = int(f.readline())
	data = [list(map(int, i.split())) for i in f]
	data.sort()
	storage = [0] * k
	count = last = 0
	for i in range(n):
		for j in range(len(storage)):
			if data[i][0] > storage[j]:
				count += 1
				storage[j] = data[i][1]
				last = j + 1
				break
print(count, last)


# 581 59
