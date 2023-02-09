i = 2
n = bin(i)[2:]
if n.count('1') % 2 == 0:
	n = n[:len(n) // 2] + '1' + n[len(n) // 2:]
	print(int(n, 2))
