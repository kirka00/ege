with open('files/27a.txt') as f:
	n, d = map(int, f.readline().split())
	data = [int(i) for i in f]
	count = 0
	for i in range(n):
		s = data[i]
		for j in range(i + 1, n):
			s += data[j]
			if data[i] == data[j] and (s - data[i] - data[j]) % d == 0 and s - data[i] - data[j]:
				count += 1
print(count)

'''
101
111215
'''

with open('files/27b.txt') as f:
	n, d = map(int, f.readline().split())
	data = [int(i) for i in f]
	count = s = 0
	slovar, l = {}, -1
	for x in data:
		s += x
		if x in slovar:
			count += slovar[x][(s - x) % d] - (x == l)
			slovar[x][s % d] += 1
		else:
			slovar[x] = [0] * d
			slovar[x][s % d] += 1
		l = x
print(count)

'''
101
111215
'''