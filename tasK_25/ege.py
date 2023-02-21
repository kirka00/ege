# нахождение делителей числа
x = 36 ** 5
ans = set()
for i in range(1, round(x ** 0.5) + 1):
	if x % i == 0:
		ans.add(i)
		ans.add(x // i)
print(ans)
