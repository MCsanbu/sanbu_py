##py=float(input("python:"))
##java=float(input("Java:"))
##if py>59.9 and java>59.9:
##    print("通过")
##else:
##    print("请继续努力")

##import random
##luck1=random.randint(0,9)
##luck2=random.randint(0,9)
##phone=int(input("输入手机尾号:"))
##print("今天手机中奖尾号为:",luck1,luck2)
##if phone ==luck1 or phone==luck2:
##    print("yes")
##else:
##    print("no")
##

for i in range(1,100):
    if i%3==2 and i%5==3 and i%7==2:
        print(i)
