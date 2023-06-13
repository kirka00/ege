p = list(range(17, 55))
q = list(range(37, 84))
a = []
for x in range(1, 100):
    if not ((x in p) <= (((x in q) and (not (x in a))) <= (not (x in p)))):
        a.append(x)
print(a)
print(54 - 37)