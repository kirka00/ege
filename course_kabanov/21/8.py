with open('files/8.txt') as f:
	s = f.readline().replace('PP', 'P P')
	s = s.split(' ')
	print(max(len(c) for c in s))