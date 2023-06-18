p = list(range(13, 20))
q = list(range(17, 24))
a = list(range(1, 1000))
for x in range(1, 1000):
    if not ((not (not (x in p)) <= (x in q)) <= ((x in a) <= ((not (x in q))) <= (x in p))):
        a.remove(x)
print(a)
