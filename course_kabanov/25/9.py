with open('files/9.txt') as f:
	n = int(f.readline())
	a = {y:set() for y in range(1961, 1992)}
	for i in range(n):
		year, stamp = map(int, f.readline().split())
		a[year].add(stamp)
    
lacks, mxLack, mxLackYear = 0, 0, 0
for year in a.keys():
    lack = 8 - len(a[year])
    if lack >= mxLack:
        mxLack = lack
        mxLackYear = year
    lacks += lack
    
print(lacks, mxLackYear)