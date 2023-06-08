for x in range(1, 100):
    s = int(f'9759{x}', 17) + int(f'3{x}108', 17)
    if s % 11 == 0:
        print(s // 11)
        break