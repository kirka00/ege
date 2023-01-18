def _func(spisok):
    res = [int(i) for i in spisok if i % 2 != 0]
    res.sort(reverse=True)
    return res


print(_func(list(map(int, input()))))
