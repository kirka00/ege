with open('24var09-13.txt') as f:
	s = f.readline().split('Z')
	mx = -1
	for i in s:
		mx = max(len(i), mx)
print(mx)

# 34 - true
