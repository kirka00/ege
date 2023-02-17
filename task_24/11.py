'''
Текстовый файл 24-s2.txt состоит не более чем из 106 заглавных латинских букв. Определите символ, который чаще всего встречается в файле между буквами A и C, так что A стоит слева от него, а C – справа. В ответе запишите сначала этот символ, а потом сразу (без разделителя) сколько раз он встретился между буквами A и C. Если таких символов несколько, нужно вывести тот, который стоит раньше в алфавите. Например, в тексте ABCCAAСZABCADCDD между буквами A и C два раза стоит B, по одному разу – A и D. Для этого текста ответом будет B2.

'''


with open('files/24-s2.txt') as f:
	s = f.readline()
	d = {}
	for i in range(len(s) - 2):
		if s[i] == 'A' and s[i + 2] == 'C':
			key = s[i + 1]
			d[key] = d.get(key, 0) + 1
	Max = max(d.values())
	for v in d.items():
		if v[1] == Max:
			print(v[0])
			print(Max)

# T72