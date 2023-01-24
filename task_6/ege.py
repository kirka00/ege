#  удобнее использоваоть Кумир
'''from turtle import *
tracer(0)
left(90)
k = 30
forward(9 * k)
right(90)
for i in range(10):
	forward(8 * k)
	left(72)
pu()
for x in range(-30, 30):
	for y in range(-30, 30):
		goto(x * k, y * k)
		dot(5)
done()
'''
'''k = 0
for x in range(300):
	for y in range(300):
		if 0 <= x <= 100 and 100 <= y <= 200:
			k += 1
print(k)'''

from turtle import *
tracer(0)
#screensize(1000, 1000)
right(90)
left(90)
k = 10
for i in range(11):
	goto(xcor() + 4 * k, ycor() + 4 * k)
	goto(xcor() - 9 * k, ycor() + 1 * k)
	goto(xcor() + 5 * k, ycor() - 5 * k)
pu()
for x in range(-k, k):
	for y in range(-k, k):
		goto(x * k, y * k)
		dot(5)
done()
