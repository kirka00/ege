for x in range(75):
	for y in range(75):
		for z in range(75):
			s = '0' + x * '1' + y * '2'+ z * '3' + '0'
			while '00' not in s:
				s = s.replace('01', '210', 1)
				s = s.replace('02', '3101', 1)
				s = s.replace('03', '2012', 1)
			if s.count('1') == 70 and s.count('2') == 56 and s.count('3') == 23:
				print(x + y + z + 2)

# 40