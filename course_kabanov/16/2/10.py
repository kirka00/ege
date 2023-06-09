s = [1] * 10_000
for n in range(len(s)):
	if n < 4:
		s[n] = 1
	if n > 3:
		if n % 2:
			s[n] = n
		else:
			s[n] = s[n - 1] + s[n - 2] + s[n - 3]
        

print(s[2254] - s[2252])