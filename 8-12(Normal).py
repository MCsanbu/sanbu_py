##m=int(input("fz:"))
##n=int(input("fm:"))
##print(m,"/",n)
##x,y=m,n
##while n>0:
##    m,n=n,m%n
##x=int(x/m)
##y=int(y/m)
##if y==1:
##    print(x)
##else:
##    print(str(x),"/",str(y))

##n=int(input("num:"))
##for j in range(n):
##    for i in range(n-j-1):
##        print(" ",end=" ")
##    for k in range(2*j+1):
##        print("*",end=" ")
##    print()

n=int(input("num:"))
list=[[1],[1,1]]
for i in range(2,n):
    p=list[i-1]
    c=[1]
    for j in range(i-1):
        c.append(p[j]+p[j+1])
    c.append(1)
    list.append(c)
print(list)
for i in range(n):
    s=" "*(n-i-1)
    for j in list[i]:
        s=s+str(j)+" "
    print(s)
