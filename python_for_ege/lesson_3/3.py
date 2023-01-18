n = int(input())
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f'{i} в степени 2 = {i ** 2}')
    else:
        print(f'{i} в степени 3 = {i ** 3}')
