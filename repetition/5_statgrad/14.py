for p in range(7, 50):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (y * p ** 2 + 4 * p + y) + (y * p ** 2 + 6 * p + 5) == x * p ** 3 + z * p ** 2 + 3 * p + 3:
                    print(p, x, y, z)
print(int('165', 8))



'''
8 1 6 5
117
'''