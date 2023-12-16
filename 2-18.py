from turtle import *
import random
import time


hideturtle()
colormode(255)

def h(a):
    for i in range(a):
        x=random.randint(-500,500)
        y=random.randint(-500,500)
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        e=random.randint(5,13)
        penup()
        goto(x,y)
        pendown()
        fillcolor(r,g,b)
        tracer(0)
        begin_fill()
        for i in range(5):
            circle(e,180)
            right(180-(360/5))
        end_fill()
        update()
        time.sleep(0.5)
    done()
