print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((not(w <= x)) or ((not z) <= (not y)) or z):
                    print(w, x, y, z)


# wzxy - true
