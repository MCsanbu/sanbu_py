##a=1
##i=1
##b=1
##while i<22:
##    a,b=b,a+b
##    i+=1
##print(b)

##i=100
##count=0
##
##while i<1000:
##    i=i+1
##    a=i//100
##    c=i%10
##    if a==c:
##         print(i)
##         count+=1
##print(count)

##num=input("num:")
##y=len(num)-1
##x=0
##palind=True
##while x<y:
##    if num[x]!=num[y]:
##        print('no num')
##        palind=False
##        break
##    else:
##        x+=1
##        y-=1
##if palind:
##    print('yes num')

from random import *

a=randint(1,10)

while True:
    b = int(input("num:"))
    if a > b:
        print("small")
    elif a < b:
        print
        

j=5
a=int(input("num:"))

if a==5:
    print("yes!!!!!!!")
else:
    print("no")

    
