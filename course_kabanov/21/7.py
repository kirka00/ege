with open('files/7.txt') as f:
	s = f.readline().replace('XY', 'X Y').replace('X Z', 'X Z')
	s = s.split()
	print(max(len(c) for c in s))
