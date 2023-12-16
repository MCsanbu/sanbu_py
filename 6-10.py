##def t(n):
##    if n==1 or n==2:
##        return 1
##    return t(n-1)+t(n-2)

##def t(n,m):
##    if m==1:
##        return n
##    return n**m

from turtle import *
pensize(10)
speed(10)
##onscreenclick(t.setpos)
##bgcolor("blue")
##pencolor("green")
##width(10)
turtlesize(2,2,2)
def up():
    forward(500)
def L():
    left(45)
def R():
    right(45)
def back():
    left(180)
    forward(50)
def reset():
    goto(0,0)
onkeypress(up,"w")
onkeypress(L,"a")
onkeypress(R,"d")
onkeypress(back,"s")
onkeypress(reset,"r")
listen()
