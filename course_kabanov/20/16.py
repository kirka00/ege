with open('files/16.txt') as f:
	s = [int(x) for x in f]
	ans_11, ans_17 = [], []
	ans_11 = [i for i in s if i % 11 == 0]
	ans_17 = [i for i in s if i % 17 == 0]
	if len(ans_11) > len(ans_17):
		print(len(ans_11), min(ans_11))
	else:
		print(len(ans_17), max(ans_17))