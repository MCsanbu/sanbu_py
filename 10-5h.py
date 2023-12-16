#1.
##a=int(input())
##print(a+1)

#2.

##a=input()
##n=len(a)
##list=[]
##for i in range(0,n):
##    list.append(a[i])
##   
##print(min(list))

#3.
a=input()
a1=0
n=a.split(",")
l=len(n)
list=[]
for i in range(0,l):
    a1=int(n[i])
    if a1<0:
        a1=a1-a1-a1
        list.append(a1)
    else:
        list.append(a1)
list.sort()

print(list)

#4.
##input1=input()
##sp=input1.split(" ")
##n=int(sp[0])
##w=int(sp[1])
##wss=0
##list=[]
##while n>0:
##    a=input()
##    lis=a.split(" ")
##    list.append(lis)
##    n=n-1
##for i in range(0,n):
##    ni=list[i][0]
##    wi=list[i][1]
##    vi=list[i][2]
##    if w>0:
##        wss=wss+ni*vi
##        w=w-wi
##    else:
##        break
##print(wss)
    
        

#5.
input1=input()
sp=input1.split(" ")
n=int(sp[0])
w=int(sp[1])
list=[]
while n>0:
    a=input()
    lis=a.split(" ")
    list.append(lis)
    n=n-1 
