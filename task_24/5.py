with open('files/24-1.txt') as f:
	s = f.readline()
	n = []
	s1 = ''
	maximun = 0
	for c in s:
		if c.isdigit():
			s1 += c
		else:
			if s1:
				n.append(s1)
			s1 = ''
	for i in n:
		if len(i) == len([x for x in i if int(x) % 2 == 0]):
			maximun = max(maximun, int(i))
print(maximun)


# 4444
