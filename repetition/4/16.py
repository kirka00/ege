s = 2030 * [1]
for n in range(1, len(s)):
	s[n] = n  + s[n - 1]

print(s[2023] - s[2019])


# 8086