with open('files/24.txt') as f:
	s = f.readline()
	s = s.replace('X', '*').replace('Y', '*').replace('Z', '*')
	while '**' in s:
		s = s.replace('**', '* *')
print(max(len(x) for x in s.split()))


# 786
