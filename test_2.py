s = 50 * '1' + 50 * '2' + 50 * '3'
while '13' in s or '32' in s or '12' in s:
    if '13' in s:
        s = s.replace('13', '31', 1)
    if '32' in s:
        s = s.replace('32', '23', 1)
    if '12' in s:
        s = s.replace('12', '21', 1)
print(s[11], s[71], s[141])


q = 143 * '7'
while '777' in q:
	q = q.replace('777', '22', 1)
	q = q.replace('222', '7', 1)
print(q)
