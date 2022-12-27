##for i in range(1,6):
##    p = 1.2 * i + 50
##    print(p)

##sum=0    
##for i in range(1,1001,1):
##    if i % 2 == 0:
##        continue
##    sum = sum + i
##print(sum)

from turtle import*


pensize(5)
speed(6)

for i in range(8):
    if i % 2 ==1:
        color("green")
    else:
        color("red")
    forward(100)
    right(360/8)

hideturtle()
done()
 
