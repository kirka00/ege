print('w x y z')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if y and (x <= w) and ((not x) <= ((not w) == z)):
					print(w, x, y, z)

print('-----------')
print('w x y z')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if not (y and (x <= w) and ((not x) <= ((not w) == z))):
					print(w, x, y, z)
