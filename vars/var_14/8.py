k = 0
for x1 in '123456789':
    for x2 in '0123456789':
        for x3 in '0123456789':
            for x4 in '0123456789':
                if (x1 == x2 and x2 != x3 and x2 != x4 and x3 != x4) or (x2 == x3 and x3 != x1 and x3 != x4 and x1 != x4) or (x3 == x4 and x3 != x2 and x3 != x1 and x1 != x2):
                    k += 1
print(k)


# 1944 - true
