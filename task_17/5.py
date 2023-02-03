with open('task_17/files/17-304.txt') as f:
    s = [int(x) for x in f]
    n = []
    for i in range(len(s) - 1):
        if (sum([int(j) for j in str(s[i])[0::2]]) \
			> sum([int(j) for j in str(s[i])[1::2]]) \
				and sum([int(j) for j in str(s[i + 1])[0::2]]) > \
					sum([int(j) for j in str(s[i + 1])[1::2]])) \
						and (abs(s[i] + s[i + 1]) % \
							(min([q for q in s[0::2]]))== 0):
            n.append(s[i] + s[i + 1])
print(len(n), min(n))
