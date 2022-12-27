##import random
##password=""
##for i in range(10):
##    password += str(random.randint(0,9))
##print(password)

x1=int(input("x1:"))
x2=int(input("x2:"))
y1=int(input("y1:"))
y2=int(input("y2:"))

d=abs(x1-x2)+abs(y1-y2)
print("曼哈顿距离:",d)
