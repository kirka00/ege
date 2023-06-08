for x in range(1, 10000):
    if int(f'3364{x}', 11) + int(f'{x}7946', 12) == int(f'55{x}87', 14):
        print(x, int(f'55{x}87', 14))