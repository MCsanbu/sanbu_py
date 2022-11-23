##from turtle import *
##def  my_abs(x):
##    for i in range(4):
##        forward(x)
##        left(90)


##from math import *
##
##def my_abs(a,b,c):
##    s=(a+b+c)/2
##    d=sqrt(s*(s-a)*(s-b)*(s-c))
##    return d

##def power(x,n=2):
##    s=1
##    while n>0:
##        n=n-1
##        s=s*x
##    return s


from turtle import *
from random import *

speed(10)
colors=['red','purple','blue','green','orange','pink','gray']

def my_abs(n):
    for i in range(n):
        x=randint(-500,500)
        y=randint(-200,200)
        v=randint(50,200)
        c=randint(0,6)
        pencolor(colors[c])
        penup()
        goto(x,y)
        pendown()
        for i in range(4):
             forward(v)
             right(90)
