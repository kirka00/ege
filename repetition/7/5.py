k = 0
for n in range(1000, 100000):
    s = str(n)
    if int(str(n)[0]) % 4 == 0:
        s = '9' + s[1:]
    if int(str(n)[0]) % 2 == 0 and int(str(n)[0]) % 4:
        s = '3' + s[1:]
    if s[0] == '9' and int(s) % 8 == 4:
         k += 1
print(k)


# 4125