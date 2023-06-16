with open("files/3.txt") as f:
	N, S = map(int, f.readline().split())
	f1 = sorted(map(int, f), reverse=True)
k, last = 0, 0
s1 = 0
while f1:
	for i in range(len(f1)):
		if f1[i] + s1 <= S:
			s1 += f1[i]
			f1[i] = 0
	f1 = [x for x in f1 if x != 0]
	k += 1
	last = s1
	s1 = 0

print(k, last)