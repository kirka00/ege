for x in '0123456789abcdefghijk':
	t = int(f'12{5}{x}9', 21) + int(f'36{5}99', 21)
	if t % 18 == 0:
		print(t // 18)
		break


# 47594 - true
