##1
from turtle import *
speed(-1)
def draw_square(length,color):
    pencolor(color)
    for i in range(4):
        forward(length)
        left(90)


##2
def Huy_be():
    for i in range(30):
        draw_square(i * 5, 'red')
        left(17)
        penup()
        forward(i * 2)
        pendown()
Huy_be()
