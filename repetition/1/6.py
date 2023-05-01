from turtle import *
left(90)
k = 10
right(180)
forward(3 * k)
right(90)
forward(48 * k)
right(90)
forward(3 * k)
for i in range(6):
    seth(90)
    circle(-4 * k, 180)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5)
done()