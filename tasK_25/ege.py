# нахождение делителей числа
x = 36 ** 5
ans = set()
for i in range(1, round(x ** 0.5) + 1):
    if x % i == 0:
        ans.add(i)
        ans.add(x // i)
print(ans)
print('-------------------------')


def prost(x):
    ans = set()
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True


k = []
for i in range(412567, 473266):
    for d in range(2, round(i ** 0.5)):
        if d * (i // d) == i and prost(d) and prost(i // d):
            k.append(i)


# ближе всего к арифметическому (метод нахождения)
sred = sum(k) / len(k)
diff = [abs(x - sred) for x in k]
ind = diff.index(min(diff))
print(len(k), k[ind])


# 12593 442939


print('----------------')
count = 0
minimum = 10 ** 10
for i in range(153732, 225675):
	for d in range(2, round(i ** 0.5)):
		if d * (i // d) == i and prost(d) and prost(i // d):
			count += 1
			if abs(i // d - d) < minimum:
				minmum = abs(i // d - d)
				q = i

print(count, q)

# 15535 473265
