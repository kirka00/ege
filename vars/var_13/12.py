s = '1' + 25 * '5'
while '15' in s or '1' in s:
	if '15' in s:
		s = s.replace('15', '5551', 1)
	else:
		if '1' in s:
			s = s.replace('1', '5', 1)
print(s.count('5'))


# 76 - true
