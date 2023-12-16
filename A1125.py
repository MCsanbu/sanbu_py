import math as m
a,b=input("").split(",")
a,b=int(a),int(b)
c=m.gcd(a,b)
print(a,"/",b)
print(a//c,"/",b//c)

