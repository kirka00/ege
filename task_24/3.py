with open('files/24-181.txt') as f:
	s = f.readline()
	kmax = 0
	for i in s.split('Y'):
		if i.count('.') <= 5:
			kmax = max(kmax, len(i))
print(kmax)

# 202
