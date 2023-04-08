for x in '0123456789abcde':
    t = int(f'97968{x}13', 15) + int(f'7{x}213', 15)
    if t % 14 == 0:
        print(t // 14)
        break


# 116070624
