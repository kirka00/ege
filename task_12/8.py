for a in range(50):
	for b in range(50):
		for c in range(50):
			s = '0' + a * '1' + b * '2' + c * '3'
			while '01' in s or '02' in s or '03' in s:
				s = s.replace('01', '2302', 1)
				s = s.replace('02', '10', 1)
				s = s.replace('03', '201', 1)
			if s.count('1') == 58 and s.count('2') == 23 and s.count('3') == 15:
				print(b)
				break
