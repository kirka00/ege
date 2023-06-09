s = [1] * 25000
for n in range(len(s)):
	if n <= 3:
		s[n] = n
	else:
		if n % 2:
			s[n] = 2 * n + s[n - 2]
		else:
			s[n] = n ** 2 + s[n - 1]
    
print(s[10_000] - s[9995])