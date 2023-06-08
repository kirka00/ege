for y in '0123456789abcdefg':
    for x in '0123456789abcde':
        s = int(f'123{x}5', 15) + int(f'67{y}9', 17)
        if s % 131 == 0:
            print(x, y, s // 131)