print('w x y z')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if (not (y and (not x))) and (not (x == z)) and w:
					print(w, x, y, z)


# yxzw
