for x in '0123456789abcde':
    for y in '0123456789abcdefg':
        s = int(f'123{x}5', 15) + int(f'67{y}9', 17)
        if s % 131 == 0:
            print(s // 131, y)
            

# 686

print('--------------')
for y in range(17):
	for x in range(15):
		d1 = 15 ** 4 + 2 * 15 ** 3 + 3 * 15  ** 2 + x * 15 + 5 
		d2 = 6 * 17 ** 3 + 7 * 17 ** 2 + y * 17 + 9
		if (d1 + d2) % 131 == 0:
				print((d1 + d2) // 131, y)