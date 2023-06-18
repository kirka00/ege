def simple(x):
	for d in range(2, round(x ** 0.5) + 1):
		if x % d == 0:
			return False
	return True




for n in range(40, 100):
	s = '0' + '1' * 122 + '2' * n + '0'
	while '00' not in s:
		s = s.replace('02', '101', 1)
		s = s.replace('11', '2', 1)
		s = s.replace('012', '30', 1)
		s = s.replace('010', '00', 1)
	if simple(sum([int(x) for x in s])):
		print(n)
		break

