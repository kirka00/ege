with open('files/21.txt') as f:
	s = f.readline()
	kmax = 0
	spisok = ['NPO', 'PNO', 'NPO', 'PNO']
	for i in range(3):
		k = 0
		for j in range(i, len(s) - 2, 3):
			if s[j] + s[j + 1] + s[j + 2] in spisok:
				k += 1
				kmax = max(kmax, k)
			else:
				k = 0
print(kmax)

