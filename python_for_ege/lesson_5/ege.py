per = 10


def _func(ar1, ar2):
    global per  # для изменения в функции
    return ar1 * ar2


print(_func(2, 3))


# проверка числа на простоту
def prosto(a):
    for i in range(1, a):
        if i % i == 0:
            return False
    return True


print(prosto(int(input())))

a = '3123123123123'
print(list(map(int, a)))


def f(n):  # рекурсия
    if n > 18:
        return n
    else:
        return 3 * f(n + 1) + n + 8


print(f(9))


# работа с файлами
with open('1.txt') as file:
    #print(file.read())
    print()
    print(file.readlines())


# 4, 5, 6 - не нужно присылать файлы
