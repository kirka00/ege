with open('files/26.txt') as f:
	n = int(f.readline())
	a = [tuple(map(int, i.split())) for i in f]
	slovar = {x: [] for x in range(1, 10001)}
	for i in a:
		if i[0] in slovar:
			slovar[i[0]].append(i[1])
	maxim = 0
	for x, y in slovar.items():
		k = kmax = 1
		spisok = sorted(set(y))
		for i in spisok:
			if spisok[i] + 1 == spisok[i + 1]:
				k += 1
				kmax = max(k, kmax)
			else:
				k = 1
			if kmax >= maxim:
				maxim = kmax
				nomer = x
print(maxim, x)
