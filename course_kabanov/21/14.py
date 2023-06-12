with open('files/14.txt') as f:
    s = f.readline()
    minim = 10 ** 10
    for i in s.split('D')[1:-1]:
        if i:
            minim = min(minim, len(i) + 2)
print(minim)