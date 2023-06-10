with open('files/26.txt') as f:
    n, m = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]
    data.sort(key=lambda x: x[0])
    free = [0] * n
    count = last = 0
    for x in data:
        if not(10 * 60 <= x[0] and 22 * 60 >= x[1]): continue
        for i in range(n):
            if x[0] >= free[i]:
                free[i] = x[1] + 1
                count += 1
                last = i + 1
                break
print(count, last)
                

# 1269 41