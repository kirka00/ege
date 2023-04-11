for x in range(1, 1000):
	s = int(f'97968{x}15', 15) + int(f'7{x}233', 15)
	if s % 14 == 0:
		print(s // 14)
		break


# 116071912
