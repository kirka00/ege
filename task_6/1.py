from turtle import *
k = 30
tracer(0)
left(90)
for i in range(10):
	right(60)
	forward(10 * k)
	right(60)
pu()
for x in range(-20, 20):
	for y in range(-20,20):
		goto(x * k, y * k)
		dot(5)
done()
