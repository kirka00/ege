for n in range(50):
	s = '6' * n
	while '66' in s:
		s = s.replace('66', '1', 1)
		s = s.replace('11', '2', 1)
		s = s.replace('22', '6', 1)
	if s == '21':
		print(n)