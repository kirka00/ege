with open('files/26-s1.txt') as f:
	n = int(f.readline())
	data = [int(i) for i in f]
	s200 = [x for x in data if x <= 200]
	ss = sorted([x for x in data if x > 200])
	skidka = ss[:len(ss) // 2]
	not_skidka = ss[len(ss) // 2:]
	print(sum(s200) + sum(skidka) * 0.7 + sum(not_skidka))
	print(max(skidka))


'''
464632
602
'''
