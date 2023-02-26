for x in '0123456789abcdefg':
    t = int(f'135{x}9', 17) + int(f'9{x}531', 17)
    if t % 9 == 0:
        print(t // 9)


# 101340 - true
