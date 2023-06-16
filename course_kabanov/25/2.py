with open("files/2.txt") as f:
	N = map(int, f.readline())
	f1 = sorted(map(int, f))
files1, files2 = [], []
while f1:
	files1.append(f1[-1])
	del f1[-1]
	while sum(files2) <= sum(files1):
		files2.append(f1[0])
		del f1[0]



print(len(files1), len(files2))