alph = '0123456789abcdefghi'
for x in alph:
	f = int(f'55{x}36', 19) + int(f'{x}2724', 19)
	if f % 11 == 0:
		print(f // 11)
		break
