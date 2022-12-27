import random
word=input("输入你的英文密码:\n").strip("")
num='abcdefghijklmnopqrstuvwxyz1234567890'
password=''
for item in word:
           new=chr(ord(item)+3)
           low=random.choice(num)
           upp=random.choice(num).upper()
           password+=upp+new+low
           print("newpassword:" ,password)
