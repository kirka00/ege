with open('files/9.txt') as f:
	s = f.readline().replace('XZZY', 'XZZ ZZY')
	s = s.split(' ')
	print(max(len(c) for c in s))