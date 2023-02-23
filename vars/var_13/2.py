print('w x y z')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if ((x == (not y)) or (x == (not z))) and w and (y <= z):
					print(w, x, y, z)

# xzyw
