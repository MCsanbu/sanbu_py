##i="to be or not to be that is a question"
##c={}
##d=0
##f=i.split(" ")
##for i in f:
##    d=f.count(i)
##    c.update({i:d})
##print(c)
##while True:
##    a=str(input("str:"))
##    b=len(a)
##    if b%2!=0:
##        print(a)
##    else:
##        print("no")
##while True:
##    a,b,c=input("num:").split(",")
##    ai=int(a)
##    bi=int(b)
##    ci=int(c)
##    d=int(ai+bi+ci)
##    if d>=60 and d<=203:
##        print("yes")
##    else:
##        print("no")
##    
s=0
k=1
for i in range(1,101):
    s=s+k*i
    k=-k
print(s)

