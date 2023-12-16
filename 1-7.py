##username="CRL"
##password="114514"
##count=0
##while count<=3:
##    user=input("请输入账号:")
##    paswd=input("请输入密码:")
##    if user==username and paswd==password:
##        print("欢迎您:",user)
##        break
##    else:
##        print("你输入错误")
##        count+=1
##        if count==3:
##            print("你的卡有异常")
##            break

a=str(input())
if a[0]=="T":
    print(a.split(" ",1))
elif a[0]=="S":
    print(a.split(" ",2))
    




