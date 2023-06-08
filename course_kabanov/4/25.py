for y in '0123456789abcdefghijk':
    for x in '0123456789abcdefghijk':
        s = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
        if s % 18 == 0:
            print(x, y, s // 18)
            

# 47594