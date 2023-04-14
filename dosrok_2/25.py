import re


for i in range(211, 10 ** 8, 211):
	if re.fullmatch('11..4.*56', str(i)):
		print(i, i // 211)
