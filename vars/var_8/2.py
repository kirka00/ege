print('w x y z') # zyxw - true
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if not(((x <= y) <= w) or (z <= (y and w))):
					print(w, x, y, z)
