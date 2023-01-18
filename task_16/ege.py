s = 2100 * [1]

for n in range(len(s)):
	if n < 4 and n % 2 != 0:
		s[n] = 1
	if n > 3 and n % 2 == 0:
		s[n] = s[n - 1] + s[n - 2] + s[n - 3]


print(s[2008] / s[2006])
