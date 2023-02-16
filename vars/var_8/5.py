
for i in range(100, 1000):
	ans = ''
	n1 = 1
	n2 = 0
	for j in str(i):
		n1 *= int(j)
		n2 += int(j)
	if n1 > n2:
		ans = str(n1) + str(n2)
	else:
		ans = str(n2) + str(n1)
	if ans == '24019':
		print(i)


# 865 - true
