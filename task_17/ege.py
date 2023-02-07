def ff(a, fun):
		return [fun(k) for k in a].count(True)


with open('task_17/files/17-1.txt') as f:
	s = [int(x) for x in f]
	n = []
	sred = sum(s) / len(s)
	for i in range(len(s) - 2):
		triple = s[i:i+3]
		if ff(triple, lambda x: x < sred) >= 2 and ff(triple, lambda x: '1' in str(x)) == 3:
			n.append(sum(triple))


print(len(n), max(n))
