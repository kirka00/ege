def simple(n):
	for d in range(2, round(n ** 0.5) + 1):
		if n % d == 0:
			return False
	return True


for a in range(50):
	for b in range(50):
		for c in range(50):
			s = '>' + a * '0' + b * '1' + c * '2'
			while '>0' in s or '>1' in s or '>2' in s:
				if '>0' in s:
					s = s.replace('>0', '22>', 1)
				if '>1' in s:
					s = s.replace('>1', '2>', 1)
				if '>2' in s:
					s = s.replace('>2', '1>', 1)
				summa = sum([int(j) for j in s if j in '0123456789'])
				if simple(summa) and s.count('0') == 15 and s.count('2') == 1:
					print(b)
					exit()
