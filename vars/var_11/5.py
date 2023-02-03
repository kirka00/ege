for n in range(1, 1000):
	u = n - (n % 4)
	s = bin(u)[2:]
	if s.count('1') % 2 == 0:
		s += '0'
	else:
		s += '1'
	if s.count('1') % 2 == 0:
		s += '0'
	else:
		s += 1
	if int(s, 2) < 64:
	 	print(int(s, 2))
