print('w x y z')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if not((not((x == y) or (x == w))) or z or (not (y <= w))):
					print(w, x, y, z)



# wyxz - true
