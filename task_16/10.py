import sys
sys.setrecursionlimit(20000)

s = 100000001 * [0]
for n in range(len(s)):
	s[n] = 8
	if n > 0 and n % 3 == 0:
		s[n] = 5 + s[n // 3]
	else:
		s[n] = s[n // 3]
print(s.count(18))
