with open('17var01.txt') as f:
	s = [int(i) for i in f]
	n = []
	for i in range(len(s) - 1):
		if abs(s[i] + s[i + 1]) == max(s):
			n.append(s[i] ** 2 + s[i + 1] ** 2)
print(len(n), max(n))
# true
# надо внимательней читать вопрос: максимальная из сумм квалратов элементов пар
