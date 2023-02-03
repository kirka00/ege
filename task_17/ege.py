with open('task_17/files/17-304.txt') as f:
	s = [int(x) for x in f]
	n = []
	min_ = min([t for t in s if t % 54 == 0])
	for i in range(len(s) - 1):
		if sum([int(j) for j in str(s[i]) if int(j) % 2 == 0]):
			n.append(s[i] + s[i + 1])
print(len(n), min(n))
print('-----------')
print('1234'[0::2])
