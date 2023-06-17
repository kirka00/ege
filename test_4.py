import re
from fnmatch import *


for i in range(17, 10 ** 9, 17):
    if re.fullmatch('23.456.89', str(i)):
        print(i, i // 17)
        
print('--------------')
for i in range(17, 10 ** 9, 17):
    if fnmatch(str(i), '23?345?89'):
        print(i, i // 17)