b = list(range(10, 16))
c = list(range(20, 28))
a = []
for x in range(1, 100):
	if (not (((x in b) or (x in c)) <= (x in a))):
		a.append(x)
print(max(a) - min(a))



# 17 - true
