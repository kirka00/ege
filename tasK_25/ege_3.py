# 1
for n in range(11000111, 11999912):
	s = str(n)
	if s[:2] == '11' and int(s[2]) % 2 == 0 and int(s[5]) % 2 and s[-2:] == '11' and n % 2023 == 0:
		print(n , n // 2023)


'''
11039511 5457
11444111 5657
11848711 5857

'''
print('--------------------')

# 1
for n in range(124065, 12994966):
	s = str(n)
	if s[:2] == '12' and s[-4] == '4' and s[-2:] == '65' and n % 161 == 0:
		print(n, n // 161)

print('----------------')
# 2
s1 = [''] + list(range(100))
for x in s1:
	for y in range(10):
		f = int(f'12{x}4{y}65')
		if f % 151 == 0:
			print(f, f // 161)
