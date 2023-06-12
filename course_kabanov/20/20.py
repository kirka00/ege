with open('files/20.txt') as f:
	s = [int(x) for x in f]
	ans = []
	summa = 0
	for q in s:
		if q % 35 == 0:
			for w in str(q):
				summa += int(w)
	for i in range(len(s) - 1):
		if (s[i] > summa and s[i + 1] < summa and hex(s[i + 1])[2:][-2::] == 'ef') or \
			(s[i] < summa and s[i + 1] > summa and hex(s[i])[2:][-2::] == 'ef'):
			ans.append(s[i] + s[i + 1])
print(len(ans), min(ans))