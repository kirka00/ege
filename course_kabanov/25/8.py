with open('files/8.txt') as f:
    l, m, n = map(int, f.readline().split())
    a = [0] * l
    for line in f:
        st, length = map(int, line.split())
        for i in range(length):
            a[st + i] = 1
s = ''.join(map(str, a))
while '11' in s: 
    s = s.replace('11','1')
s = [len(x) for x in s.split('1') if len(x) >= m]
print(len(s), max(s))