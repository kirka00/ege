alph = '0123456789abc'
for x in alph:
	f = int(f'8{x}121', 13) - int(f'7{x}575', 13)
	if f % 19 == 0:
		print(f // 19)
		break


for x in range(2, 36):
	if int('13', x) * int('31', x) == int('423', x):
		print(x)
