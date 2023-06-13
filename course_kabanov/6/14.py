c = list(range(1, 12, 2))
b = list(range(3, 13, 3))
a = []
for x in range(1, 100):
    if not (((x in c) <= (not (x in b))) or (x in a)):
        a.append(x)
print(sum(a))
