k = 0


def F(n):
    global k
    k += 1
    if n >= 1:
        k += 1
        F(n-1)
        F(n//3)
        k += 1
    return k

print(F(280))
