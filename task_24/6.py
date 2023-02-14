from fnmatch import *
with open('files/24-228.txt') as f:
	s = f.readline().split('SS')[1:-1]
	ch = '0123456789'
	ans = []
	for x in s:
		if len(x) == 11 and x[0:2] == '12' and x[2] in ch \
			and x[3] in ch and x[4] in ch  and x[5] in ch and x[6] in ch and \
				x[6:8] == '77' and x[8] in ch and x[9] in ch and \
					x[10] in ch and x[-1] == '9':
			ans.append(x)

pr = 1
summa = 0
for i in max(ans):
	if int(i) % 2:
		summa += int(i)
	else:
		pr *= int(i)

print(pr + summa)


# 49183
