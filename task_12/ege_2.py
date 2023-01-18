'''k = 0
s = 400 * '5'
while '555' in s or '333' in s:
	if '555' in s:
		s = s.replace('555', '3', 1)
		k += 3
	else:
		s = s.replace('333', '5', 1)
print(k)
'''

'''
for a in range(50):
	for b in range(50):
		for c in range(50):
			s = '0' + a * '1' + b * '2' + c * '3'
			while '01' in s or '02' in s or '03' in s:
				s = s.replace('01', '2302', 1)
				s = s.replace('02', '10', 1)
				s = s.replace('03', '201', 1)
			if s.count('1') == 51 and s.count('2') == 29 and s.count('3') == 23:
				print(c)
				break
'''

'''
k = set()
for i in range(2, 100):
	s = i * '5'
	while '555' in s or '888' in s:
		s = s.replace('555', '8', 1)
		s = s.replace('888', '55', 1)
	k.add(s)
print(len(k))
'''

for n in range(41, 100):
    s = '>' + n * '0' + n * '1' + n * '2'
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '00>', 1)
        if '>0' in s:
            s = s.replace('>0', '11>', 1)
        s = s.replace('>0', '11>', 1)
    if sum([int(i) for i in s if i != '>']) % 100 == 77:
        print(n)
        break
