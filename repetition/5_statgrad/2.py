print('w x y z 1 2')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				print(w, x, y, z, int((x or (not y)) == (z <= w)), int(((not x) == y) and (z <= w)))



'''
Ответ: zxyw
w x y z 1 2
0 0 0 0 1 0
0 0 0 1 0 0
0 0 1 0 0 1
0 0 1 1 1 0
0 1 0 0 1 1
0 1 0 1 0 0
0 1 1 0 1 0
0 1 1 1 0 0
1 0 0 0 1 0
1 0 0 1 1 0
1 0 1 0 0 1
1 0 1 1 0 1
1 1 0 0 1 1
1 1 0 1 1 1
1 1 1 0 1 0
1 1 1 1 1 0
'''