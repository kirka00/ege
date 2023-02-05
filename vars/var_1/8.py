from itertools import product

stek = product('01234567', repeat=5)
ans = set()
for i in stek:
    i = ''.join(i)
    if i.count('4') == 2 and i[0] != '0' and \
            '14' not in i and \
    		'41' not in i and \
			'34' not in i and \
			'43' not in i and \
			'54' not in i and \
			'45' not in i and \
			'74' not in i and \
			'47' not in i and \
			'94' not in i and \
				'49' not in i:
        ans.add(i)
print(len(ans))
# true
