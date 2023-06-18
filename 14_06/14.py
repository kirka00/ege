for x in '0123456789abc':
    s = int(f'537{x}623', 13) + int(f'6{x}35{x}2', 13)
    if s % 3 == 0:
        print(x)
        
print(int('c', 13))