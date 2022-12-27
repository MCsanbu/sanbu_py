from random import randint

a = randint(0,100)

b = eval(input("猜数:"))


while True:
    if b > a:
        print("太大")
        break
    elif b < a:
        print("太小")
        break
    elif b == a:
        print("你猜中了！")
        break 
    else:
        print("bfjdjdj")
        break 







