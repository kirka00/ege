with open('files/26-53.txt') as f:
	n = int(f.readline())
	s = [int(i) for i in f]
	s1 = set(s)
	ans = []
	for i in range(len(s) - 1):
		for j in range(i + 1, len(s)):
			if s[i] % 2 == 0 and s[j] % 2 == 0 and (s[i] + s[j]) / 2 in s1:
				ans.append((s[i] + s[j]) / 2)

print(len(ans), min(ans))
