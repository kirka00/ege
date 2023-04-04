with open('files/3.txt') as f:
    s = f.readline()
    print(s.count('OCK') - s.count('STOCK'))
