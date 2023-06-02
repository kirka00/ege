import re


for i in range(253, 10 ** 8, 253):
    if re.fullmatch('12..15.*6', str(i)):
        print(i, i // 253)



"""
1278156 5052
12531596 49532
12741586 50362
12951576 51192
"""