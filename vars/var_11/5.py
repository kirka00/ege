answer = []
for n in range(1000):
	n = n % 4
	s = bin(n)[2:]
	if s.count('1') % 2 == 0:
		s += '0'
	else:
		s += '1'
	if s.count('1') % 2 == 0:
		s += '0'
	else:
		s += 1
	if int(s, 2) < 64:
		answer.append(int(s, 2))
print(max(answer))
