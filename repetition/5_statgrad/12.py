def simple(x):
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True


for n in range(100, 200):
    s = '0' + n * '1' + n * '2' + '0'
    while '00' not in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('12', '21', 1)
        s = s.replace('010', '00', 1)
    if simple(sum(map(int, s))):
        print(n)
        break
        

# 104