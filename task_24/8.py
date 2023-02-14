with open('files/24-5.txt') as f:
	s = f.readline()
	k = 0
	for i in range(len(s)):
		if s[i] == '(' and s[i + 1] == ')':
			k += 1
		if k == 10000:
			print(i + 1)
			break


# 40451
