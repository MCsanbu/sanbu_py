##a=int(input("num:"))
##i=1
##while i<a:
##    if a%i==0:
##        print("not 素数")
##        break
##    i+=1
##else:
##    print("yes 素数")

##a=2
##c=0
##while a<=100:
##    i=2
##    while i<a:
##        if a%i==0:
##            break
##        i+=1
##    else:
##        c+=1
##        print(a)
##    a+=1
##print(c)

a=int(input("num:"))
for i in range(a+1):
    for j in range(a-i):
        print(" ",end=" ")
    for z in range(2*i-1):
        print("*",end=" ")
    print()
