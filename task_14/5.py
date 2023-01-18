x = 53 ** 123 + 65 ** 2222 - 172 ** 12
s = ''
while x > 0:
	s = str(x % 7) + s
	x //= 7
print(s.count('61') + s.count('62') +
      s.count('63') + s.count('64') + s.count('65'))
