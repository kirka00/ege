with open("files/2.txt") as f:
	D, E, N = map(int, f.readline().split())
	f1 = sorted(map(int, f))


d_files, e_files = [], []
for i in f1:
	if i > 500:
		if sum(d_files) + i <= D:
			d_files.append(i)
	else:
		if sum(e_files) + i <= E:
			e_files.append(i)
        
print(d_files, e_files)
print(len(d_files) + len(e_files), max(d_files) + max(e_files))