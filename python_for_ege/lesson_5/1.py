def _func(n):
    spisok = list(map(int, str(n)))
    res = [i for i in spisok if i % 2 != 0]
    return len(res), sum(res)


print(_func(int(input())))
