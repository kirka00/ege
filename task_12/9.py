for a in range(50):
	for b in range(50):
		for c in range(50):
			s = '0' + a * '1' + b * '2' + c * '3' + '0'
			while not '00' in s:
				s = s.replace('01', '21022', 1)
				s = s.replace('02', '310', 1)
				s = s.replace('03', '230112', 1)
			if s.count('1') == 104 and s.count('2') == 39 and s.count('3') == 83:
				print(a + b + c + 2)
				break
