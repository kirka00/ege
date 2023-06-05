with open('files/17.txt') as f:
	s = [int(i) for i in f]
	k, minnim, mx = 0, 10 ** 10, 0
	m = min([x for x in s if x % 8 == 0 and x != 8])
	for i in range(len(s) - 1):
		if s[i] % m == 0 and s[i + 1] % m == 0:
			k += 1
			if (s[i] + s[i + 1]) < minnim:
				minnim = s[i] + s[i + 1]
				mx = max(s[i], s[i + 1])
print(k, mx)

# 3 74280