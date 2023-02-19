a = [1] * 40
for i in range(3, 40):
	if i % 2:
		a[i] = a[i - 1] - a[i - 2]
	else:
		a[i] = sum(a[1:i])
print(a[39])


# 41518080 - true
