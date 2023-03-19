with open('files/dz_5/b.txt') as f:
	n = int(f.readline())
	x = []
	for i in range(n):
		x.append(int(f.readline()))
	mi1, mi2, mi3 = [10 ** 10] * 4, [10 ** 10] * 4, [10 ** 10] * 4
	mi = 10 ** 10
	for i in range(n):
		d = x[i] % 4
		mi = min(mi, x[i] + mi3[(4 - d) % 4])
		mi3nov = mi3
		for k in range(4):
			d0 = (k + d) % 4
			mi3nov[d0] = min(mi3[d0], mi2[k] + x[i])
		mi3 = mi3nov
		mi2nov = mi2
		for k in range(4):
			d0 = (k + d) % 4
			mi2nov[d0] = min(mi2[d0],  mi1[k] + x[i])
		mi2 = mi2nov
		mi1[d] = min(mi1[d], x[i])
	print(mi)


# 1320 404632
