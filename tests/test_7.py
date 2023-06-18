b = list(range(20, 31))
c = list(range(70, 91))
q = []
for a in range(1000, 1, -1):
	for x in range(1, 101):
		if not((x + 11 > a) or ((x in b) <= (x % 7 != 0)) or (x in c)):
			q.append(x)

print(max(q))


