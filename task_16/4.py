s = [0] * 10 ** 6
for n in range(len(s)):
	if n <= 3:
		s[n] = n
	else:
		if n % 2 == 0:
			s[n] = n + s[n - 1]
		else:
			s[n] = n * n + s[n - 2]

print(len([i for i in range(len(s)) if 1 <= s[i] 	< 10 ** 8]))
