with open('files/24-s1.txt') as f:
   k = 0
   for s in f:
       for i in range(len(s) - 3):
           if s[i] == 'F' and s[i + 2] == 'O':
               k += 1
               break
print(k)


# 757
