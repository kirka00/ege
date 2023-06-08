for x in range(1, 100):
    s = int(f'123{x}5', 15) + int(f'1{x}233', 15)
    if s % 14 == 0:
        print(s // 14)
        break