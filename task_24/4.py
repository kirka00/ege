with open('files/24-191.txt') as f:
	s = f.readline().split('A')[1:-1]
	k = 0
	for i in s:
		if len(i) >= 15 and 'B' not in i:
			k += 1
print(k)

# 597
