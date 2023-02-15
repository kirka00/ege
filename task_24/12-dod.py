with open('files/24-164.txt') as f:
	MA = 0
	for s in f:
		k = 1
		ma = 0
		for i in range(len(s)-1):
			if s[i] == s[i+1]:
				k += 1
			else:
				ma = max(ma,k)
				k = 1
		if ma > MA:
			mi = 1000000000000
			e=''
			for p in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				if s.count(p) <= mi and s.count(p) != 0:
					mi =s.count(p)
					e = p
		MA = ma


with open('files/24-164.txt') as f:
	m = 0
	for s in f:
		m = m + s.count(e)
print(e)
print(m)
