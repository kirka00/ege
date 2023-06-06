with open('files/26.txt') as f:
	n, l, m = map(int, f.readline().split())
	data = []
	for i in range(n):
		start, time, type_ = f.readline().split()
		data.append((int(start), int(time) + int(start), type_))
	data.sort()
	busy = [0] * (l + m)
	count = countB = 0
	for x in data:
		place0 = 0 if x[-1] == 'A' else l
		for place in range(place0, l + m):
			if x[0] >= busy[place]:
				busy[place] = x[1]
				countB += (x[2] == 'B')
				break
		else:
			count += 1
print(countB, count)        


# 430 35