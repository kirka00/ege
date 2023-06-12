with open('files/18.txt') as f:
    s = f.readline().replace('KOT', '*').replace('K', ' ').replace('O', ' ').replace('T', ' ')
    print(max(len(i) for i in s.split()))
    