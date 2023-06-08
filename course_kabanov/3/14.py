from itertools import permutations

k = set()
for i in permutations('дейкстра', r=6):
	w = ''.join(i)
	if ('йд' in w or'йк' in w or 'йс' in w or 'йт' in w or'йр' in w):
		k.add(w)


print(len(k))


# 9000