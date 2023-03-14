for i in range(103_000_000, 104_000_001):  # более-менее быстрый алгоритм
	count = 1
	sqr = round(i ** 0.5)
	if i % 2 == 0:
		for j in range(2, sqr + 1):
			if i % j == 0:
				if j % 2 == 0:
					count += 1
				if (i // j) % 2 == 0:
					count += 1
				if j != 2:
					k = j
			if count > 3:
				break
	if count == 3:
		print(i, k)
		count = 1


''' Долго считает
def prost(n):
	count = 1
	k = 0
	for i in range(2, round(n ** 0.5) + 1):
		if n % i == 0:
			if i % 2 == 0:
				count += 1
			if (n // i) % 2 == 0:
				count += 1
			if i != 2:
				k = i
		if count > 3:
			break
	return count, k


for i in range(103_000_000, 104_000_001):
	f = prost(i)
	if f[0] == 3:
		print(i, f[1])
'''


''' Ответ
103018658 7177
103305938 7187
103478498 7193
103881698 7207
103997042 7211
'''
