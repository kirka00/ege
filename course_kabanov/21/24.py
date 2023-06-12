with open('files/24.txt') as f:
	s = f.readline()
	line = 'CA'
	while line in s:
		line += 'CA'
	while line not in s:
		line = line[:-1]
	print(len(line))

