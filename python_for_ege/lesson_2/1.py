a, b, c = list(map(int, input("Введите числа в одну строку: ").split()))

if a > b and a < c:
    print(a)
elif b > a and b < c:
    print(b)
else:
    print(c)
