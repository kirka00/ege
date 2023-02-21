for x in range(251811, 251827):
	ans = set()
	for d in range(1, round(x ** 0.5) + 1):
		if x % d == 0:
			ans.add(d)
			ans.add(x // d)
			if len(ans) > 4:
				break
	if len(ans) == 4:
		print(sorted(ans)[2:])


'''
[8123, 251813]
[50363, 251815]
[83939, 251817]
[601, 251819]
[14813, 251821]
'''
