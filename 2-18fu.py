from turtle import *
import random
import time


hideturtle()
colormode(255)
fillcolor(255,192,203)

def h(a):
    for i in range(a):
        x=random.randint(-200,200)
        y=random.randint(-200,200)
        penup()
        goto(x,y)
        pendown()
        tracer(0)
        begin_fill()
        for i in range(5):
            circle(10,180)
            right(180-(360/5))
        end_fill()
        update()
        time.sleep(0.5)
    done()
