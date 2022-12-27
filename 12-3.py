##for i  in range(3):
##    if i==1:
##        continue
##    print(i)
##else:
##    print("s")

##for i in range(1,11):
##    for j in range(1,i):
##        print(j,end=" ")
##    print()
##else:
##    print("done")

##import random
##num=["b","a","iphone14","$1000W"]
##a=random.choice(num)
##random.shuffle(num)
##print(a)

from turtle import *
speed(9)
pencolor("yellow")
bgcolor('red')
shape("turtle")
up()
goto(-240,200)
down()
fillcolor("yellow")
begin_fill()
for i in range(5):
    forward(50)
    left(72)
    forward(50)
    right(144)
end_fill()

up()
goto(-150,50)
down()
right(36)
begin_fill()
for i in range(5):
    forward(30)
    left(72)
    forward(30)
    right(144)
end_fill()

up()
goto(50,80)
down()
begin_fill()
for i in range(5):
    forward(30)
    left(72)
    forward(30)
    right(144)
end_fill()

up()
goto(0,50)
down()
begin_fill()
for i in range(5):
    forward(30)
    left(72)
    forward(30)
    right(144)
end_fill()

up()
goto(0,50)
down()
begin_fill()
for i in range(5):
    forward(30)
    left(72)
    forward(30)
    right(144)
end_fill()
