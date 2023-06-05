with open('files/26.txt') as f:
    n, k = map(int, f.readline().split())
    data = []
    for x in f:
        size, color = x.split()
        data.append([int(size), color])
    data.sort(reverse=True)
    count = 0
    max_block = - 1
    flag = 0
    while data:
        if flag == 0:
            count_block = 0
            last_cont = [10 ** 10, '']
            count += 1
        flag = 0
        for i in range(len(data)):
            if last_cont[0] - data[i][0] >= k and last_cont[1] != data[i][1]:
                last_cont = data[i]
                flag = 1
                count_block += 1
                max_block = max(max_block, count_block)
                del data[i]
                break
            
print(count, max_block)

# 25 2093
            