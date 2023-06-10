ans = set()
for n in range(1, 50):
	s = n * '5'
	while '555' in s or '888' in s:
		s = s.replace('555', '8', 1)
		s = s.replace('888', '55', 1)
	ans.add(s)
print(len(ans))