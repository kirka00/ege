s = 2100 * [1]

for n in range(len(s)):
	if n == 1:
		s[n] = 1
	else:
		s[n] = n * s[n - 1]


print(s[2023] / s[2020])
