for x in '0123456789abc':
    s = int(f'8{x}121', 13) - int(f'7{x}575', 13)
    if s % 19 == 0:
        print(s // 19)
        break
    

# 1464