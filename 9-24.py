# while嵌套循环

i=0

while i<6:
    j=0
    while j<i:
        print(j*" ",i*"*",j*" ")
        j=j+1
    print()
    i=i+1


