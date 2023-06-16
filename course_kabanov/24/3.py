with open("files/3.txt") as f:
	N, M = map(int, f.readline().split())
	f1 = sorted(map(int, f))


files, flag = [], True
for i in f1:
	if flag:
		if i >= 101:
			if sum(files) <= M // 2:
				files.append(i)
			else:
				flag = False
	else:
		if i <= 100:
			if sum(files) + i <= M:
				files.append(i)
        

print(M - sum(files), len(files))