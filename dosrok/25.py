import re

for x in range(273, 10 ** 8, 273):
    if re.fullmatch('12..36.*1', str(x)):
        print(x, x // 273)

print('---------------------')
for x in range(1200361, 12993692):
    s = str(x)
    if x % 273 == 0 and s[0:2] == '12' and s[4:6] == '36' and s[-1] == '1':
        print(x, x // 273)

'''
1271361 4657
12633621 46277
12663651 46387
12693681 46497
'''
