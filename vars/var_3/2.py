print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not (y <= (not (z <= w)))) and ((not z) <= ((not w) == x)):
                    print(w, x, y, z)

print('---------------------')
print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not ((not (y <= (not (z <= w)))) and ((not z) <= \
					((not w) == x))):
                    print(w, x, y, z)
