s = 4 * 25 ** 2022 - 2 * 5 ** 2000 + 125 ** 1011 - 3 * 5 ** 100 - 660
new = ''
while s > 0:
	new += str((s % 5))
	s //= 5
print(new.count('4'))
# true
