for x in range(8):
	for y in range(8):
		s = int(f'{y}04{x}5', 11) + int(f'253{x}{y}', 8)
		if s % 117 == 0:
			print(s // 117) 

# 224


print('----')
for x in range(8):
	for y in range(8):
		d1 = y * 11 ** 4 + 0 + 4 * 11 ** 2 + x * 11 + 5
		d2 = 2 * 8 ** 4 + 5 * 8 ** 3 + 3 * 8 ** 2 + x * 8 + y
		s = d1 + d2
		if s % 117 == 0:
			print(s // 117) 
