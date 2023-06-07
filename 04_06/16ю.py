s = 30000 * [1]
for n in range(1, len(s)):
	if n >= 2222:
		s[n] = n
	if n < 2222:
		s[n] = n ** 3  + s[n + 2]

print(s[4] - s[10])


# -936