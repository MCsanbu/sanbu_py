from turtle import *
def f(color):
    x=-300
    y=300
    fillcolor(color)
    tracer(0)
    for i in range(8):
        for j in range(8):
            goto(x+i*n,y+j*n)
            if(i+j)%2==0:
                f("white")
            else:
                f("black")
    update()
