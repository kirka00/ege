import re

for i in range(17, 10**9, 17):
    if re.fullmatch('12345.6.8', str(i)):
        print(i, i // 17)