def f(x):
	divs = set()
	for d in range(2, round(x ** 0.5) + 1):
		if x % d == 0:
			divs.add(d)
			divs.add(x // d)
	return len(divs)

for m in range(1, 555):
	s = '>' + 17 * '1' + 34 * '2' + m * '3'
	while '>1' in s or '>2' in s or '>3' in s:
		if '>1' in s:
			s = s.replace('>1', '22>')
		if '>2' in s:
			s = s.replace('>2', '2>')
		if '>3' in s:
			s = s.replace('>3', '1>')
	summa = sum(int(i) for i in s if i != '>')
	if f(summa) == 3:	
		print(m)
		break


# 489