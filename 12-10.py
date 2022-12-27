##a=int(input("num:"))
##while a!=1:
##    if a%2!=0:
##        a=a*3+1
##        print(a)
##    else:
##        a=a/2
##        print(a)
##password=555555
##user=int(input("password:"))
##a=1
##while a<7:
##    if user==password:
##        print("Welcome")
##        break
##    elif user!=password:
##        print("你的密码已输错%d次"%a)
##        a+=1
##        user=int(input("password:"))
##else:
##    print("你的卡被锁死")
##



count=0
for a in range(10000,100000):
    b=a//10000
    c=a%10000//1000
    d=a%10000%1000//100
    e=a%10000%1000%100//10
    f=a%10000%1000%100%10
    if b==f and c==e:
        print(a)
        count=count+1
print(count)
