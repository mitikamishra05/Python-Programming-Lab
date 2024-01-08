import turtle as t
t.pen()
t.bgcolor("black")
colors=["red","green","yellow","blue","gray",
"purple","aqua","brown",]
name=t.textinput("Enter your name",
"Enter your name")
s=int(t.numinput("number of sides",
"how many sides you want(1-20)",10,1,20))
for i in range(100):
    t.pencolor(colors[i%s%10])
    t.penup()
    t.forwad(i*5)
    t.pendown()
    t.write(name,font=("",
    int((i*2+4)/4),"bold"))
    t.left(360/s+4)