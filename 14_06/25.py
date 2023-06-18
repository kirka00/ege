for i in range(2468035, 10 ** 9):
    if int(str(i)[2]) % 3 == 0 and i % 13 == 0 and str(i)[0:2] == '24' and str(i)[3:5] == '68' and str(i)[5:7] == '35':
        print(i, i // 13)
        

# ?