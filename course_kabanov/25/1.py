f = open("files/1.txt")
S, N = map(int, f.readline().split())

f1 = sorted(map(int, f))
flag = True
save_files = []
while True:
	if flag:
		if sum(save_files) + f1[-1] <= S:
			save_files.append(f1[-1])
			del f1[-1]
			flag = False
		else:
			break
	else:
		if sum(save_files) + f1[0] <= S:
			save_files.append(f1[0])
			del f1[0]
			flag = True
		else:
			break

print(save_files)

print(len(save_files), save_files[-1])