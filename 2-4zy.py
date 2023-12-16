from turtle import *
import time

bgcolor("hot pink")
hideturtle()
pencolor("gray")

for x in range(-100,100,10):
    goto(x,0)
    clear()
    tracer(0)
    fillcolor("green")
    begin_fill()
    circle(15)
    end_fill()
    
    penup()
    goto(x+15,25)
    pendown()
    fillcolor("red")
    begin_fill()
    circle(10)
    end_fill()
    
    penup()
    goto(x-15,25)
    pendown()
    fillcolor("blue")
    begin_fill()
    circle(10)
    end_fill()
    
    update()
    time.sleep(0.05)
done()
