x = int(input())
r = int(input())
x2 = x
while r >= x:
    print(x)
    x += 1
print(f"В промежутке от X до R {r - x2 + 1} чисел")
