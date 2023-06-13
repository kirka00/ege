import re

for i in range(51, 10 ** 6, 51):
    if re.fullmatch('12.*45.*', str(i)):
        print(i, i // 51)