with open('files/dz_5/b.txt') as f:
	n = int(f.readline())
	data = [int(i) for i in f]
	minim = 10 ** 10
	minim1, minim2, minim3 = [0] * 4, [0] * 4, [0] * 4
	for i in data:
		ostat = i % 4
		minim = min(minim, i + minim3[(4 - ostat) % 4])
		for d in range(4):
			ostat0 = (d + ostat) % 4
			minim3[ostat0] = min(minim3[ostat0], minim2[d] + i)
			minim2[ostat0] = min(minim2[ostat0], minim1[d] + i)
		minim1[ostat] = min(minim1[ostat], 	i)
print(minim)


# 206 100278
