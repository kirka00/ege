summa = 0
for n in range(2, 11):
    x = 572
    s = ''
    while x > 0:
        s = str(x % n) + s
        x //= n
    if '00' in s or '11' in s or '22' in s or '33' in s or '44' in s or '55' in s or '66' in s or '77' in s or '88' in s or '99' in s:
        summa += n
print(summa)
