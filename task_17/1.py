with open('task_17/files/17-4.txt') as f:
	s = [int(x) for x in f]
	n = []
	for c in s:
		if c % 3 == 0 and c % 9 != 0 and 4 <= c % 10 :
			n.append(c)
sred = sum(n) // len(n)
print(len(n), sred)
