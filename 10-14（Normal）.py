##c=0
##list=[]
##list1=[]
##i=2
##for i in range(2,1001):
##    j=2
##    for j in range(2,i):
##        if i%j==0:
##            break
##    else:
##            if i%3==2:
##                list.append(i)
##            elif i%7==6:
##                list.append(i)
##            elif i%11==10:
##                list.append(i)
##            elif i%17==16:
##                list.append(i)
##            elif i%23==22:
##                list.append(i)
##list1=list[:10]
##print(list1)

##a=[]
##n=input()
##l=len(n)
##for i in range(0,l):
##    a.append(n[i])
##for j in a:
##    if j>"W":
##        print(chr(ord(j)-23))
##    else:
##        o=ord(j)
##        c=chr(o+2)
##        print(c)

a=input()
num=int(input())
for i in range(num):
    for j in range(num-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print(a,end="")
        else:
            print(" ",end="")
    print()
for i in range(num,1,-1):
    for j in range(num-i+1):
        print(" ",end="")
    for j in range(2*i-1):
        if j==0 or j==2*i-4:
            print(a,end="")
        else:
            print(" ",end="")
    print()
