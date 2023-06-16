with open('files/8.txt') as f:
    l, m, n = map(int, f.readline().split())
    a = [0] * (l + 1)
    for _ in range(n):
        st, l = map(int, f.readline().split())
        a[st] += 1
        a[st + l] -= 1
        
k = 0
st, end = 0, 0
count, ml = 0, 0
for i in range(l + 1):
    k0 = k
    k += a[i]
    if k == 0 and st == 0:
        st = i
    if (k == 1 and k0 == 0) or i == l:
        end = i
        lenght = end - st
        if lenght >= m:
            count += 1
            ml = max(ml, lenght)
        st, end = 0, 0
print(count, ml)
        
        
		