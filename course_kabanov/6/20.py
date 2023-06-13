b = list(range(18, 53))
c = list(range(16, 42))
a = []
for x in range(1, 100):
    if not (((x in b) <= (x in a)) and ((not (x in c)) or (x in a))):
        a.append(x)
print(a)
print(52 - 16)