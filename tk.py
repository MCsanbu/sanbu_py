from tkinter import *
import random as ra
def sb():
    print("test")
def a():
    def random(w,h,fc):
        x=ra.randrange(w)
        y=ra.randrange(h)
        x1=ra.randrange(w)
        y1=ra.randrange(h)
        c.create_rectangle(x,y,x1,y1,fill=fc)
    for x in range(0,100):
        random(800,800,None)
tk=Tk()
c=Canvas(tk,width=1000,height=1000)#画布
b=Button(tk,text="555555555555555555555555",command=a)#按钮
##c.create_line(0,0,500,500)
##c.create_rectangle(15,15,50,100)
c.create_arc(10,10,200,543,extent=270,style=ARC)
c.create_polygon(100,300,150,500,600,300,100,400,300,400,outline=("black"))
b.pack()
c.pack()
     
