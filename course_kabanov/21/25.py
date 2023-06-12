with open('files/25.txt') as f:
	s = f.readline()
	line = 'DBAC'
	while line in s:
		line += 'DBAC'
	while line not in s:
		line = line[:-1]
	print(len(line))

