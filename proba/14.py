for x in '0123456789abcde':
    s = int(f'99658{x}29', 15) + int(f'102{x}023', 15)
    if s % 14 == 0:
        print(s // 14)


# 118330623