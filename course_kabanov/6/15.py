c = list(range(3, 13, 3))
b = list(range(1, 7))
a = []
for x in range(1, 100):
    if not ((not ((not (x in a)) and (x in c))) or (not (x in b))):
        a.append(x)
print(len(a))
