##a=0
##while a<9:
##    a+=1
##    b=1
##    while b<a+1:
##        print(a,"*",b,"=",a*b,end=" ")
##        b+=1
##    print()

n=int(input("num:"))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for a in range(1,2*i):
        print("*",end=" "
    print()
