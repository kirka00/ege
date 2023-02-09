for i in range(100, 1000):
	n = str(i)
	s1 = int(n[0]) ** 2 + int(n[1]) ** 2
	s2 = int(n[1]) ** 2 + int(n[2]) ** 2
	if s1 > s2:
		new = str(s1) + str(s2)
	else:
		new = str(s2) + str(s1)
	if '9752' == new:
		print(i)


# 946 - true
