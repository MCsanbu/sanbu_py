myid={"name:":"Billy","Age:":11,"like:":"programme"}
myid.update(m=99)
print(myid)
del myid['m']
print(myid)
for i,j in myid.items(): 
    print(i,j)
