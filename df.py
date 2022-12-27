##for x in range(4,0,-1):
##    print(x)

##海龟画图
from turtle import *
from random import randint

pensize(8)
speed(6)


for i in range(5):
    R=randint(0,255)
    G=randint(0,255)
    B=randint(0,255)
    colormode(255)
    color(R,G,B)
    forward(100)
    left(360/5)

hideturtle()
done()

##from turtle import *
##
##pensize(6)
##speed(6)
##
##
##for i in range(8):
##    forward(134)
##    left(360/8)
##
##hideturtle()
##done()

##from turtle import *
##from random import randint
##
##pensize(7)
##speed(6)
##
##for i in range (3):
##    R=randint(0,255)
##    G=randint(0,255)
##    B=randint(0,255)
##    colormode(255)
##    color(R,G,B)
##    forward(70)
##    left(360/3)
##
##hideturtle()
##done()
