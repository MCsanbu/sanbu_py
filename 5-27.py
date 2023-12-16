##for i in range(2,101):
##    for j in range(2,i):
##        if i%j==0:
##            print(i,"不是")
##            break
##    else:
##        print(i)

from turtle import *
import random
bgcolor("black")
speed(10)
shape("turtle")
co=["red","yellow","grey","orange","pink","green","white","purple","silver","gold",]

def a(r):
    tracer(0)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(5):
        left(72)
        forward(r)
        right(144)
        forward(r)
    end_fill()
    update()
def u(e):
    tracer(0)
    penup()
    goto(x1,y1)
    pendown()
    begin_fill()
    for i in range(4):
       circle(e,90)
       right(180)
    end_fill()
    update()
for i in range(100):
    x=random.randint(-600,600)
    y=random.randint(-400,400)
    x1=random.randint(-600,600)
    y1=random.randint(-400,400)
    c=random.randint(5,75)
    d=random.randint(0,9)
    fillcolor(co[d])
    pencolor(co[d])
    a(c)
    u(c)
    hideturtle()
