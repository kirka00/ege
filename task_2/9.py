print('a b c')
for a in range(2):
	for b in range(2):
		for c in range(2):
			if not ((a and c) or ((not a) and (b or (not c)))):
				print(a, b, c)


'''
a b c
0 0 1
1 0 0
1 1 0  
'''
