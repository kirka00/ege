with open('files/24-164.txt') as f:
	maximum = 0
	for x in f:
		if x.count('E') < 20:
			for i in x:
				maximum = max(maximum, x.rindex(i) - x.index(i))
print(maximum)


with open('files/24-s1.txt') as f:
	k = 0
	for x in f:
		for i in range(len(x) - 2):
			if x[i] == 'F' and x[i + 2] == 'O':
				k += 1
print(k)


# 1493
