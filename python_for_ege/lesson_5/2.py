def fact(n):
    k = 1
    for i in range(1, n + 1):
        k *= i
    return k


print(fact(int(input())))
