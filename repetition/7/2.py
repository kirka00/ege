print('w x y z F')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				print(w, x, y, z, int((x == (z <= y)) and (not w)))
    
'''
wyzx
w x y z F
0 0 0 0 0
0 0 0 1 1
0 0 1 0 0
0 0 1 1 0
0 1 0 0 1
0 1 0 1 0
0 1 1 0 1
0 1 1 1 1
1 0 0 0 0
1 0 0 1 0
1 0 1 0 0
1 0 1 1 0
1 1 0 0 0
1 1 0 1 0
1 1 1 0 0
1 1 1 1 0
'''