with open('files/26.txt') as f:
    n = f.readline()
    data = [int(i) for i in f]
    data.sort(reverse=True)
    flag, count, max_block = True, 0, -1
    while data:
        if flag:
            count_block = 0
            last_cont = 10 ** 10
            count += 1
        flag = True
        for i in range(len(data)):
            if last_cont - data[i] >= 5:
                last_cont = data[i]
                flag = False
                count_block += 1
                max_block = max(max_block, count_block)
                del data[i]
                break
            
print(count, max_block)
            

# 17 1767
    