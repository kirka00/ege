import re

for i in range(0, 10 ** 10 + 1, 50068):
    if re.fullmatch('9.979.*8', str(i)) and '0' in str(i):
        print(i, i // 50068)
        

'''
9097906348 181711
9297928008 185706
'''