print('w x y z')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if ((w == (not y) or (w == (not z)))) and x and (y <= z):
					print(w, x, y, z)


# xwyz - true
