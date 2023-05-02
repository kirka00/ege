def nosimple(a):
    for x in range(2, int(a ** 0.5) + 1):
        if a % x == 0:
            return True
    return False



i = 350_001
k = 0
while k != 6:
    divs = set()
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    if len(divs) != 0:
        if nosimple(max(divs)):
            k += 1
            print(i, max(divs))
    i += 1

'''
350001 116667
350002 175001
350004 175002       
350007 116669       
350008 175004       
350009 31819 
'''