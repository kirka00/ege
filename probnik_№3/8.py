alf = ['с', 'а', 'л', 'ь']
q = 0
for a1 in alf:
	for a2 in alf:
		for a3 in alf:
			for a4 in alf:
				for a5 in alf:
					for a6 in alf:
						word = a1 + a2 + a3 + a4 + a5 + a6
						if word.count('а') <= 1:
							q += 1
print(q)


# 2187
