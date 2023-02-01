x = 4 ** 700 + 4 ** 100 - 16 ** 100 - 64
s = ''
while x > 0:
	s = str(x % 4) + s
	x //= 4
print(s.count('3'))
