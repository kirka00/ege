'''
Текстовый файл 24-s2.txt состоит не более чем из 106 заглавных латинских букв. Определите символ, который чаще всего встречается в файле между буквами A и C, так что A стоит слева от него, а C – справа. В ответе запишите сначала этот символ, а потом сразу (без разделителя) сколько раз он встретился между буквами A и C. Если таких символов несколько, нужно вывести тот, который стоит раньше в алфавите. Например, в тексте ABCCAAСZABCADCDD между буквами A и C два раза стоит B, по одному разу – A и D. Для этого текста ответом будет B2.

'''


with open('files/24-s2.txt') as f:
	minA = 10 ** 20
	slovar = {}
	for line in f:
		countA = line.count('A')
		if countA < minA:
			minA = countA
			s = line
	for x in s:
		if x in slovar:
			slovar[x] += 1
		else:
			slovar[x] = 1
	alph = []
	for y in slovar.items():
		if max(slovar.values()) == y[1]:
			alph.append(y[0])
with open('files/24-s1.txt') as f:
	print(f.read().count(max(alph)))
