print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((not ((x == y) or (x == z))) or w or (not (y <= z))):
                    print(w, x, y, z)


# xwyz - true
