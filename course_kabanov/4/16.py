for x in range(1, 40):
    if bin(x)[2:][-4::] == '1011':
        print(x)
