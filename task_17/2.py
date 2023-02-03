with open('task_17/files/17-205.txt') as f:
	s = [int(x) for x in f]
	n = []
	for i in range(len(s) - 1):
		if (s[i] % 7 == 0 or s[i + 1] % 7 == 0) and (abs(s[i] + s[i + 1]) % 5 == 0):
			n.append(s[i] + s[i + 1])
print(len(n), max(n))
