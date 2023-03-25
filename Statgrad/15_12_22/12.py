from itertools import product
data = product('12', repeat=20)
ans = []
for i in data:
	s = ''.join(i)
	if s.count('1') == s.count('2') == 10:
		j = '0' + s + '0'
		while '00' not in j:
			j = j.replace('012', '30', 1)
			if '011' in j:
				j = j.replace('011', '20', 1)
				j = j.replace('022', '40', 1)
			else:
				j = j.replace('01', '10', 1)
				j = j.replace('02', '101', 1)
		if j.count('1') == 7 and j.count('2') == 5:
			ans.append(j.count('3'))
print(min(ans))


# 3
