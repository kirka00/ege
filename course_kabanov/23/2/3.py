import re

for i in range(169, 10 ** 9, 169):
    if re.fullmatch('123.*567.', str(i)):
        print(i, i // 169)