with open('files/26-73.txt') as f:
	n = int(f.readline())
	a = [tuple(map(int, i.split())) for i in f]
	slovar = {x: [] for x in range(1, 641)}
	for i in a:
		if i[0] in slovar:
			slovar[i[0]].append(i[1])
	maxim = 0
	for x, y in slovar.items():
		k = kmax = 1
		spisok = sorted(set(y))
		for i in range(len(spisok) - 1):
			if spisok[i] + 1 == spisok[i + 1]:
				k += 1
				kmax = max(k, kmax)
			else:
				k = 1
			if kmax >= maxim:
				maxim = kmax
				nomer = x
print(maxim, x)


with open('files/26-66.txt') as f:
	n, start = map(int, f.readline().split())
	end = start + 24 * 3600 * 1000
	milliseconds = {i: 0 for i in range(start, end + 1)}
	files = [list(map(int, i.split())) for i in f]
	for x in files:
		if (x[0] < end or x[0] == 0) and (x[1] > start or x[1] == 0):
			if (x[0] == 0 or x[0] < start):
				x[0] = start
			if (x[1] == 0 or x[1] > end):
				x[1] = end
			milliseconds[x[0]] += 1
			milliseconds[x[1]] -= 1
	k = kmax = 0
	for i in milliseconds.items():
		k += i[1]
		if k > kmax:
			kmax = k
			count = 0
		if k == kmax:
			count += 1
print(kmax, count)
