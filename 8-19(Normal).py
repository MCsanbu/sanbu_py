list=[]
a=0
for i in range(5):
    a=int(input("num:"))
    list.append(a)
l=len(list)
for i in range(0,l):
    for j in range(i+1,l):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
a0=list[0]
for i in list:
    if i-a0!=0:
        print(a0)
    else:
        a0 +=1
##while True:
##    d=0
##    n=int(input())
##    a=0
##    b=0
##    c=0
##    for a in range(1,n):
##        for b in range(a,n):
##            for c in range(b,n):
##                if a+b+c==n:
##                    if a>=b and b>=c and a>=c:
##                        d+=1
##    print(d)

##dic={0:"零",1:"壹",2:"贰",3:"叁",4:"肆",5:"伍",6:"陆",7:"柒",8:"捌",9:"玖"}
##a=0
##shu=input()
##for i in shu:
##    a=int(i)
##    print(dic.get(a),end="")
