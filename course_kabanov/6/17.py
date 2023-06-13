p = list(range(2, 21, 2))
q = list(range(3, 31, 3))
r = list(range(12, 61, 12))
a = []
for x in range(1, 100):
    if not((x not in a) <= (((x in p) and (x in q)) <= (x in r))):
        a.append(x)
print(a)
print(6 * 18)