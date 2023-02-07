def pyat(x):
	new = ''
	while x > 0:
		new += str(x % 5)
		x //= 5
	return new

with open('task_17/files/17-324.txt') as f:
	s = [int(x) for x in f]
	n = []
	spisok = [t for t in s if t % 31 == 0]
	sred_31 = sum(spisok) / len(spisok)
	for i in range(len(s) - 2):
		triple = sum(s[i:i+3])
		sred = sum(s[i:i+3]) / len(s[i:i+3])
		if (str(pyat(triple)) == str(pyat(triple))[::-1]) and sred > sred_31:
			n.append(sum(s[i:i+3]))

print(len(n), min(n))
