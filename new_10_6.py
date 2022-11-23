##for i in range(1,10):
##    for j in range(i,10):
##        print(i,"*",j,"=",i*j,end=" ")
##    print()


##count=0
##
##for a in [1,2,3,4]:
##    for b in [1,2,3,4]:
##        for c in [1,2,3,4]:
##            if a!=b and c!=b and a!=c:
##                count=count+1
##                print(a,b,c)
##print(count)

for i in range(0,21):
    for j in range(0,34):
        if 5*i+3*j+(100-i-j)/3==100:
            print(i,j,100-i-j)


##from turtle import *
##
##colors=['red','purple','blue','green','yellow','orange','pink','gray']
##
##speed(0)
##
##bgcolor('black')
##
##for x in range(360):
##    pencolor(colors[x%8])
##    width(x/100+1)
##    forward(x)
##    left(49)

##from turtle import *
##
##colors=['red','purple','blue','green','yellow','orange','pink','gray']
##
##speed(0)
##bgcolor('black')
##sides=8
##
##for x in range(360):
##    pencolor(colors[x%sides])
##    width(x*sides/100+1)
##    forward(x*3/sides+x)
##    left(360/sides+1)
##    
