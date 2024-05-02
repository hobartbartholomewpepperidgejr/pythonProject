import tkinter

def gencoords(x, y, scale=1):
    global coordlist, blank
    coordlist = []
    global xmax, ymax
    xmax = x-1
    ymax = y-1
    for width in range(0, x):
        for height in range(y, -1, -1):
            exec("x" + str(width) + "y" + str(height) + " = tkinter.Label(text='', bg='white', textvariable='', width="+str(2*scale)+", height="+str(1*scale)+")", globals())
            exec("x" + str(width) + "y" + str(height) + ".grid(column=" + str(width) + ", row=" + str(abs(height-(y+1))) + ", sticky='nesw')", globals())
            exec("coordlist.append('" + "x" + str(width) + "y" + str(height)+ "')", globals())

def coordconstructor(x, y):
    return "x"+str(x)+"y"+str(y)

def spritecomp(c, offx=0, offy=0):
    result=[]
    y = 0
    for i in c.order:
        current=eval("c."+str(i))
        for x in range(len(current)):
            if current[x]=="#":
                result.append("x"+str(x+offx)+"y"+str(y+offy))
        y += 1
    for i in result:
        eval(i).config(textvariable=c.__name__)
    return(result)

def drawsprite(c, color="black"):
    for i in spritecomp(c, offy=c.y, offx=c.x):
        eval(i).config(bg=color)

def move(s, x=0, y=0):
    if spacecheck(s, x, y):
        if s.x + x >= 0 and s.x + x <= xmax:
            s.x += x
        if s.y + y >= 0 and s.y + y <= ymax:
            s.y += y
    else:
        print("collision")
        raise Exception("sprite collision")

def screensave(screen):
    eval("screen" + screen + "=[]")
    for i in ct.coordlist:
        if eval(i)["bg"] != "white" and eval(i)["textvariable"] != "sprite":
            eval("screen"+screen+".append('#')")
        else:
            eval("screen" + screen + ".append('.')")

def spacecheck(s, x=0, y=0):
    try:
        tomove = []
        name = s.__name__
        w = 0
        for i in coordlist:
            if eval(i)["textvariable"] == name:
                tomove.append(i)
        for i in tomove:
            a = int(i[i.index("x") + 1:i.index("y")]) + x
            b = int(i[i.index("y") + 1:]) + y
            if eval(coordconstructor(a, b))["textvariable"] != "" and eval(coordconstructor(a, b))["textvariable"] != name:
                w = 1
            elif coordconstructor(a, b) in coordlist:
                w = 1
        if w == 1:
            return False
        else:
            return True
    except:
        return False


def coordsplitter(coord):
    a = int(coord[coord.index("x") + 1:coord.index("y")])
    b = int(coord[coord.index("y") + 1:])
    print(a, b)
    return a, b