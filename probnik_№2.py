'''print('w x y z')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if not(((x <= z) <= y) or (not w)) :
					print(w, x, y, z)'''

'''def f(x, y):
	if x > y:
		return 0
	if x == y:
		return 1
	return f(x + 1, y) + f(x + 3, y)



print(f(3, 12) * f(12, 20))'''

'''def f(x, p):  # 19
	if x > 37 or p > 3:
		return p == 3
	if p % 2:
		return f(x + 1, p + 1) and f(x + 2, p + 1) and f(x + 3, p + 1) \
			and f(x * 2, p + 1)
	else:
		return f(x + 1, p + 1) or f(x + 2, p + 1) or f(x + 3, p + 1) \
				or f(x * 2, p + 1)

print(min([i for i in range(1, 38) if f(i, 1)]))


def f(x, p):  # 20
	if x > 37 or p > 3:
		return p == 3
	if p % 2 == 0:
		return f(x + 1, p + 1) or f(x + 2, p + 1) or f(x + 3, p + 1) \
			or f(x * 2, p + 1)
	else:
		return f(x + 1, p + 1) and f(x + 2, p + 1) and f(x + 3, p + 1) \
				and f(x * 2, p + 1)


print([i for i in range(1, 38) if f(i, 0)])


def f(x, p):  # 21
	if x > 37 or p > 5:
		return p == 3 or p == 5
	if p % 2 == 0:
		return f(x + 1, p + 1) or f(x + 2, p + 1) or f(x + 3, p + 1) \
			or f(x * 2, p + 1)
	else:
		return f(x + 1, p + 1) and f(x + 2, p + 1) and f(x + 3, p + 1) \
				and f(x * 2, p + 1)


print(min([i for i in range(1, 38) if f(i, 1)]))'''
'''k = 0
def F(n):
	global k
	k += 1
	if n >= 1:
		k += 1
		F(n-1)
		F(n-2)

print(F(28))
print(k)'''
'''
# 13
x = 25 ** 56 + 5 ** 138 - 5
s = ''
while x != 0:
    s += str(x % 5)
    x //= 5
print(s.count("4"))'''

'''# 14
for a in range(1, 100):
    k = 0
    for x in range(1, 1000):
        if (x % a == 0) <= ((x % 14 == 0) and (x % 21 == 0)):
            k += 1
    if k == 999:
        print(a)
        break'''

'''
for a in range(50):
	for b in range(50):
		for c in range(50):
			s = '0' + a * '1' + b * '2' + c * '3' + '0'
			while '00' not in s:
				s = s.replace('01', '210', 1)
				s = s.replace('02', '3101', 1)
				s = s.replace('03', '2012', 1)
			if s.count('1') == 111 and s.count('2') == 101 and s.count('3') == 35:
				print(a + b + c + 2)
				break
'''
'''
k = set()
for i in range(1, 1000):
    s = bin(i)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += 1
    if int(s, 2) < 50:
        k.add(s)
print(len(k))'''
