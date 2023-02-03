with open('task_17/files/17-304.txt') as f:
	s = [int(i) for i in f]
	n = []
	for i in range(len(s) - 1):
		if sum([int(j) for j in str(s[i]) if int(j) % 2 != 0]) > sum([int(j)
			for j in str(s[i]) if int(j) % 2 == 0]) and \
				sum([int(j) for j in str(s[i + 1]) if int(j) % 2 != 0]) > \
					sum([int(j) for j in str(s[i + 1]) \
						if int(j) % 2 == 0]) and (s[i] + s[i + 1]) % \
								min([i for i in s if i % 2 != 0]) == 0:
			n.append(s[i] + s[i + 1])
print(len(n), min(n))
