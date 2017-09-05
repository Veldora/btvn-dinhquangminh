##3
from turtle import *
speed(-1)
def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)


##4
def minh_dep_trai():
    speed(0)
    color('blue')
    for i in range(100):
        import random
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        length = random.randint(3, 10)
        draw_star(x, y, length)
minh_dep_trai()
