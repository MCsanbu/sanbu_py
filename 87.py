##buy=int(input("price:"))
##W=0
##
##if buy>500:
##    W=buy*0.5
##elif buy>300:
##      W=buy*0.75
##elif buy>=100:
##      W=buy*0.9
##elif buy<100:
##      W=buy
##print(W)
##
##ER=int(input("maths:"))
##if ER==3:
##    print("Boss")
##elif ER==2:
##    print("User")
##elif ER==1:
##    print("Worker")
##elif ER==0:
##    print("Error")
##else:
##    print("Roadman")
##       
##
X = int(input("X:"))
Y = int(input("Y:"))
Z = input("+,-,*,/ :")
W = 0

if Z == "+":
    W = X + Y
    print(W)
elif Z == "-":
    W = X - Y
    print(W)
elif Z== "*":
    W = X * Y
    print(W)
elif Z == "/":
    W = X / Y
    print(W)
else:
    print("ERROR")
    
