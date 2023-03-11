with open('files/17.txt') as f:
	s = [int(x) for x in f]
	n = []
	chisla = [i for i in s if i % 37 == 0]
	summa = 0
	for q in chisla:
		for w in str(q):
			summa += int(w)
	for i in range(len(s) - 1):
		if (s[i] > summa and s[i + 1] > summa):
			n.append(s[i] + s[i + 1])
print(len(n), min(n))
