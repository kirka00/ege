import re


for i in range(3023, 10 ** 10, 3023):
	if re.fullmatch('1.954.*21', str(i)):
		print(i)



'''
1895421
1295437121
1395498421
1795441321
'''