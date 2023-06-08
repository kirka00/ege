from itertools import permutations

k = set()
for i in permutations('вайфу', r=4):
	w = ''.join(i)
	if w[0] != 'й' and 'вф' not in w and 'фв' not in w:
		k.add(w)


print(len(k))


# 68