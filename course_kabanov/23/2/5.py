import re

for i in range(2023, 10 ** 10, 2023):
    if re.fullmatch('1.2139.*4', str(i)):
        print(i, i // 2023)