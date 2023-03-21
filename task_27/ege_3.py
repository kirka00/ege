def osob(x):
	x = -x
	if x <= 0:
		return False
	sum3 = 0
	while x:
		sum3 += x % 3
		x //= 3
	if sum3 == 12:
		return True


with open('files/10/27-91a.txt') as f:
	n, k, d = map(int, f.readline().split())
	maxsum = - 10 ** 9
	tailsum = [[10 ** 9] * d for i in range(k)]
	summa = count = countosob = 0
	for i in range(n):
		x = int(f.readline())
		summa += x
		count += 1
		ostat = count % d
		if osob(x):
			countosob += 1
		ostatosob = countosob % k
		if ostatosob == ostat == 0 and summa > maxsum:
			maxsum = summa
		if tailsum[ostatosob][ostat] != 10 ** 9 and summa - tailsum[ostatosob][ostat] > maxsum:
			maxsum = summa - tailsum[ostatosob][ostat]
		tailsum[ostatosob][ostat] = min(tailsum[ostatosob][ostat], summa)
print(maxsum)
