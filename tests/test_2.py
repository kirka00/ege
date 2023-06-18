def f(x, y):
    return (3 * x + 4 * y != 60) or ((a >= x) and (a >= y))


for a in range(1, 1000):
	if all(f(x, y) == True for x in range(1, 1000) for y in range(1, 1000)):
		print(a)
		break



from itertools import product

k = set()
for i in product('01234567889', repeat=6):
	q = ''.join(i)
	if q[-23:-1] == '26' and q[0] != '0' and \
		q.count('0') == 1 and \
		q.count('1') == 1 and \
		q.count('2') == 1 and \
		q.count('3') == 1 and \
		q.count('4') == 1 and \
		q.count('5') == 1 and \
		q.count('6') == 1 and \
		q.count('7') == 1 and \
		q.count('8') == 1 and \
		q.count('9') == 1 and \
		((q.count('0') + q.count('2') + q.count('4') + q.count('6') + \
   		q.count('8') == 3) or (q.count('1') + q.count('3') + q.count('5') + \
		q.count('7') + q.count('9') == 2)):
		k.add(q)
print(q)
