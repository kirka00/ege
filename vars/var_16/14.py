for x in '0123456789abcdefghijklmnop':
	for y in '0123456789abcdefghijklmnop':
		if y == '2':
			t = int(f'13{y}{x}5', 26) + int(f'24{y}13', 26)
			if t % 8 == 0:
				print(t // 8)


# 187162 - true
