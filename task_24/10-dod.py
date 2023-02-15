with open('files/24-s1.txt') as f:
	k = 0
	for x in f:
		for i in range(len(x) - 3):
			if x[i] == 'F' and x[i + 3] == 'O':
				k += 1
print(k)


# 1495
