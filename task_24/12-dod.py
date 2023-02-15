with open('files/24-164.txt') as f:
    kmax = 0
    count = 0
    n = -1
    for s in f.readlines():
        count += 1
        k = 1
        for i in range(0, len(s) - 1):
            if s[i] == s[i+1]:
                k += 1
                if k > kmax:
                    kmax = k
                    n = count
            else:
                k = 1

with open('files/24-164.txt') as f:
	count = 0
	a = [0] * 150

	for s in f.readlines():
		count = count+1
		if count == n:
			for i in range(0, len(s)):
				a[ord(s[i])] += 1

	print(a)

	ch = ''
	mn = 0
	for i in range(0, 150):
		if a[i] > mn:
			mn = a[i]
			ch = chr(i)

	print(ch)

with open('files/24-164.txt') as f:
	print(f.read().count(ch))
