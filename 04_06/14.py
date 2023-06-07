for x in '0123456789abcdefgh':
    s = int(f'77968{x}11', 18) + int(f'4{x}213', 18)
    if s % 7 == 0:
        print(s // 7)
        

# 648833380	