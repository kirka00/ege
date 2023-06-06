from math import gcd

# hard
with open('files/27a.txt') as f:
	n = int(f.readline())
	data = [int(x) for x in f]
	count = 0
	for i in range(n - 25):
		for j in range(i + 25, n):
			if (data[i] + data[j]) % 4 == 0 and (data[i] * data[j]) % 9009 == 0:
				count += 1
print(count)


'''
289
'''


with open('files/27b.txt') as f:
	n = int(f.readline())
	data = [int(x) for x in f]
	count = 0
	divs = [d for d in range(1, 9001 + 1) if 9009 % d == 0]
	pairs = [{d: 0 for d in divs} for i in range(4)]
	q = []
	for i in range(n):
		if len(q) >= 25:
			ff = q.pop(0)
			r = ff % 4
			d = gcd(ff, 9009)
			pairs[r][d] += 1
		if data[i] % 4 == 0:
			rr = 0
		else:
			rr = 4 - data[i] % 4
		for d in divs:
			if d * data[i] % 9009 == 0:
				count += pairs[rr][d]
		q.append(data[i])
print(count)