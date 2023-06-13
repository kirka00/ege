import re

for i in range(141, 10 ** 8, 141):
    if re.fullmatch('1234.*7', str(i)):
        print(i, i // 141)