for i in range(1000):
	n = bin(i)[2:]
	if n.count('1') % 2 == 0:
		n = n[:len(n) // 2] + '1' + n[len(n) // 2:]
	if int(n, 2) >= 26:
		print(i)
		break


# 12 - true
