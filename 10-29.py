##import random
##list=[]
##
##for i in range(3):
##    a=random.randint(1,10)
##    list.append(a)
##list.sort()
##print(list)

##h=float(input("height:"))
##w=float(input("weight:"))
##bmi=w/(h**2)
##
##if bmi<18.5:
##    print(bmi,"过轻")
##elif bmi>=18.5 and bmi<25:
##    print(bmi,"正常")
##elif bmi>=25 and bmi<28:
##    print(bmi,"过重")
##elif bmi>=28 and bmi<32:
##    print(bmi,"肥胖")
##elif bmi>=32:
##    print(bmi,"严重肥胖")

##from turtle import *
##
##fillcolor("yellow")
##
##begin_fill()
##circle(50)
##end_fill()

for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end=" ")
    print()
