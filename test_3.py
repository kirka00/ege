# 1	
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0)):
            k += 1
    if k == 999:
        print(a)
        break



# 2
def f(x):
    return ((a % 40 == 0) and ((780 % x == 0) <= ((a % x) <= (180 % x))))


for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		print(a)
		break


# 3
def f(x):
    return (((72 % x == 0) <= (120 % x)) or (a - x > 100))

for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		print(a)
		break


# 4
def f(x):
    return (((72 % x == 0) <= (90 % x)) or (a -x > 90))

for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		print(a)
		break


'''
1 - 12
2 - 960
3 - 125
4 - 109
'''



# 1
print(bin(4 ** 2020 + 2 ** 2017 - 15)[2:].count('1'))
# 2015

# 14 задание
s = 9 ** 8 + 3 ** 5 - 9
n = ''
while s > 0:
	n += str(s % 3)
	s //= 3
print(n.count('2'))
# 3

# 3
s = 2 * 216 ** 6 + 3 * 36 ** 9 - 432
n = ''
while s > 6:
	n += str(s % 6)
	s //= 6
print(n.count('5'))
# 14