print('w x y z')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if x and (y <= z) and ((not y) <= ((not z) == w)):
					print(w, x, y, z)

print('--------------')
print('w x y z')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if not (x and (y <= z) and ((not y) <= ((not z) == w))):
					print(w, x, y, z)
