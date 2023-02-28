def prost(x):
	for d in range(2, round(x ** 0.5) + 1):
		if x % d == 0:
			return False
	return True


i = 650_001
k = 0
while k != 4:
	divs = set()
	for d in range(2, i):
		if i % d == 0 and prost(d):
			divs.add(d)
	if len(divs):
		if (sum(divs) // len(divs)) % 37 == 23:
			k += 1
			print(i, sum(divs) // len(divs))
	i += 1




'''
650090 60
650153 282
650155 3945
650208 134
'''
