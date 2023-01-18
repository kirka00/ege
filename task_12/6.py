for i in range(82, 1000):
    s = '1' * i
    while '11' in s:
        s = s.replace('11', '2', 1)
        s = s.replace('2222', '111', 1)
    if s == '2221':
        print(i)
        break
