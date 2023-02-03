with open('task_17/files/17-1.txt') as f:
	s = [int(x) for x in f]
	n = []
	sred = sum(s) / len(s)
	for i in range(len(s) - 1):
		if (s[i] > sred and s[i + 1] > sred) and abs(s[i] + s[i + 1]) % 100 == 31:
			n.append(s[i] + s[i + 1])
print(len(n), max(n))
