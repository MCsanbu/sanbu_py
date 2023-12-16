from turtle import *
import time

bgcolor("black")
hideturtle()
fillcolor("blue")
for x in range(-300,301,50):
    for y in range(0,100,10):
        goto(x,y)
        clear()
        tracer(0)
        begin_fill()
        circle(99)
        end_fill()
        update()
        time.sleep(0.1)
done()
