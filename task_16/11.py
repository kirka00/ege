import sys
sys.setrecursionlimit(20000)

s = 500000001 * [0]
for n in range(len(s)):
    s[n] = 1
    if n > 0 and n % 2 != 0:
        s[n] = 1 + s[n - 1]
    else:
        s[n] = s[n // 2]
print(s.count(4))
