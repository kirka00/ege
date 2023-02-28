def prost(x):
	for d in range(2, round(x ** 0.5) + 1):
		if x % d == 0:
			return False
	return True


k = 1
for i in range(2532421, 2532492):
	if prost(i):
		print(k, i)
		k += 1


'''
1 2532433
2 2532437
3 2532449
4 2532451
5 2532479
6 2532487
'''
