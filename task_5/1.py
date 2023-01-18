for i in range(1000, 10000):
    s = str(i)
    sum1 = int(s[0]) + int(s[1])
    sum2 = int(s[2]) + int(s[3])
    if sum1 > sum2:
        final = str(sum2) + str(sum1)
    else:
        final = str(sum1) + str(sum2)
    if final == '117':
        print(i)
