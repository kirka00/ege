with open("files/1.txt") as f:
    S, N = map(int, f.readline().split())
    f1 = sorted(map(int, f), reverse=True)

save_files = []
for i in f1:
    if sum(save_files) + i <= S:
        save_files.append(i)


print(len(save_files), save_files[-1])