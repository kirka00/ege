with open('files/24.txt') as f:
	s = f.readline()
	for i in 'ABC':
		s = s.replace(i, '+')
	for i in '123':
		s = s.replace(i, '!')
	s = s.replace('!+!', '*')
	k = kmax = 0
	for c in s:
		if c == '*':
			k += 1
			kmax = max(kmax, k)
		else:
			k = 0
print(kmax)


# 164