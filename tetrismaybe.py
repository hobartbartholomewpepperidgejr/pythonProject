import tkinter, random
import coordtools as ct
window=tkinter.Tk()
ct.gencoords(10, 20)
class gamestorage:
    tetraminoes=["T", "E", "L", "I", "S"]
    currentx=5
    currenty=20
    tetraminocoords=[]
    occupiedcoords=[]
    currenttetramino = tetraminoes[random.randint(0, 4)]
    tcolor = ["pink", "yellow", "orange", "blue", "green"]
    orientation = 0
    key = ""
    score = 0

def keypress(event):
    if event.keysym == "a" or event.keysym == "d" or event.keysym == "s":
        print(event.keysym)
        gamestorage.key = event.keysym
        event.keysym = 0


def gentetraminocoords(name, xoff = 0, yoff = 0): # generation data
    x = gamestorage.currentx + xoff
    y = gamestorage.currenty + yoff
    if name == "T":
        if gamestorage.orientation == 0:
            return ct.coordconstructor(x - 1, y),\
                    ct.coordconstructor(x, y),\
                    ct.coordconstructor(x+1, y),\
                    ct.coordconstructor(x, y-1)
        elif gamestorage.orientation == 1:
            return ct.coordconstructor(x, y+1),\
                    ct.coordconstructor(x, y),\
                    ct.coordconstructor(x + 1, y),\
                    ct.coordconstructor(x, y - 1)
        elif gamestorage.orientation == 2:
            return ct.coordconstructor(x, y + 1),\
                    ct.coordconstructor(x - 1, y),\
                    ct.coordconstructor(x, y),\
                    ct.coordconstructor(x + 1, y)
        elif gamestorage.orientation == 3:
            return ct.coordconstructor(x, y+1),\
                    ct.coordconstructor(x, y),\
                    ct.coordconstructor(x - 1, y),\
                    ct.coordconstructor(x, y - 1)
    elif name == "E":
        if gamestorage.orientation == 0:
            return ct.coordconstructor(x, y),\
                    ct.coordconstructor(x + 1, y),\
                    ct.coordconstructor(x, y - 1),\
                    ct.coordconstructor(x + 1, y - 1)
        elif gamestorage.orientation == 1:
            return ct.coordconstructor(x, y), \
                   ct.coordconstructor(x + 1, y), \
                   ct.coordconstructor(x, y - 1), \
                   ct.coordconstructor(x + 1, y - 1)
        elif gamestorage.orientation == 2:
            return ct.coordconstructor(x, y), \
                   ct.coordconstructor(x + 1, y), \
                   ct.coordconstructor(x, y - 1), \
                   ct.coordconstructor(x + 1, y - 1)
        elif gamestorage.orientation == 3:
            return ct.coordconstructor(x, y), \
                   ct.coordconstructor(x + 1, y), \
                   ct.coordconstructor(x, y - 1), \
                   ct.coordconstructor(x + 1, y - 1)
    elif name == "L":
        if gamestorage.orientation == 0:
            return ct.coordconstructor(x, y),\
                    ct.coordconstructor(x, y - 1),\
                    ct.coordconstructor(x, y - 2),\
                    ct.coordconstructor(x + 1, y - 2)
        elif gamestorage.orientation == 1:
            return ct.coordconstructor(x+1, y-1), \
                   ct.coordconstructor(x,y-1), \
                   ct.coordconstructor(x-1, y-1), \
                   ct.coordconstructor(x - 1, y - 2)
        elif gamestorage.orientation == 2:
            return ct.coordconstructor(x-1, y), \
                   ct.coordconstructor(x, y), \
                   ct.coordconstructor(x, y-1), \
                   ct.coordconstructor(x, y - 2)
        elif gamestorage.orientation == 3:
            return ct.coordconstructor(x+1, y), \
                   ct.coordconstructor(x-1, y - 1), \
                   ct.coordconstructor(x, y - 1), \
                   ct.coordconstructor(x+1, y - 1)
    elif name == "I":
        if gamestorage.orientation == 0:
            return ct.coordconstructor(x, y), \
                   ct.coordconstructor(x, y - 1), \
                   ct.coordconstructor(x, y - 2), \
                   ct.coordconstructor(x, y - 3)
        elif gamestorage.orientation == 1:
            return ct.coordconstructor(x-2, y-1), \
                   ct.coordconstructor(x-1, y-1), \
                   ct.coordconstructor(x, y-1), \
                   ct.coordconstructor(x+1, y-1)
        elif gamestorage.orientation == 2:
            return ct.coordconstructor(x, y), \
                   ct.coordconstructor(x, y - 1), \
                   ct.coordconstructor(x, y - 2), \
                   ct.coordconstructor(x, y - 3)
        elif gamestorage.orientation == 3:
            return ct.coordconstructor(x - 2, y - 1), \
                   ct.coordconstructor(x - 1, y - 1), \
                   ct.coordconstructor(x, y - 1), \
                   ct.coordconstructor(x + 1, y - 1)
    elif name == "S":
        if gamestorage.orientation == 0:
            return ct.coordconstructor(x, y), \
                   ct.coordconstructor(x, y - 1), \
                   ct.coordconstructor(x + 1, y - 1), \
                   ct.coordconstructor(x + 1, y - 2)
        elif gamestorage.orientation == 1:
            return ct.coordconstructor(x+1, y), \
                   ct.coordconstructor(x, y), \
                   ct.coordconstructor(x, y-1), \
                   ct.coordconstructor(x-1, y-1)
        elif gamestorage.orientation == 2:
            return ct.coordconstructor(x, y), \
                   ct.coordconstructor(x, y - 1), \
                   ct.coordconstructor(x + 1, y - 1), \
                   ct.coordconstructor(x + 1, y - 2)
        elif gamestorage.orientation == 3:
            return ct.coordconstructor(x + 1, y), \
                   ct.coordconstructor(x, y), \
                   ct.coordconstructor(x, y - 1), \
                   ct.coordconstructor(x - 1, y - 1)

def gentetramino(color = None):
    if color == None:
        color = gamestorage.tcolor[gamestorage.tetraminoes.index(gamestorage.currenttetramino)]
    tetramino = gamestorage.currenttetramino
    for coords in gentetraminocoords(tetramino):
        exec("ct." + str(coords) + ".config(bg='"+str(color)+"')")
    gamestorage.currenttetramino = str(tetramino)
    return gentetraminocoords(tetramino)

ct.gencoords(10,20)
gentetramino()


def movecheck(direction):
    w = 0
    if direction == "left":
        for i in gentetraminocoords(gamestorage.currenttetramino, -1):
            if i in gentetraminocoords(gamestorage.currenttetramino):
                print(i)
            elif eval("ct." + i + "['bg']") != "white":
                w = 1
        if w == 0:
            return True
        else:
            raise Exception("requested direction occupied or invalid")
    if direction == "right":
        for i in gentetraminocoords(gamestorage.currenttetramino, 1):
            if i in gentetraminocoords(gamestorage.currenttetramino):
                print(i)
            elif eval("ct." + i + "['bg']") != "white":
                w = 1
        if w == 0:
            return True
        else:
            raise Exception("requested direction occupied or invalid")
    if direction == "down":
        for i in gentetraminocoords(gamestorage.currenttetramino, 0, -1):
            if i in gentetraminocoords(gamestorage.currenttetramino):
                print(i)
            elif eval("ct." + i + "['bg']") != "white":
                w = 1
        if w == 0:
            return True
        else:
            raise Exception("requested direction occupied or invalid")

def turncheck(direction):
    w = 0
    temp = gamestorage.orientation
    if direction == "left":
        if gamestorage.orientation == 3:
            gamestorage.orientation = 0
        else:
            gamestorage.orientation += 1
    if direction == "right":
        if gamestorage.orientation == 0:
            gamestorage.orientation = 3
        else:
            gamestorage.orientation -= 1
    a = gentetraminocoords(gamestorage.currenttetramino)
    gamestorage.orientation = temp
    b = gentetraminocoords(gamestorage.currenttetramino)
    for i in a:
        if i in b:
            print(i)
        elif eval("ct." + i + "['bg']") != "white":
            w = 1
    if w == 0:
        return True
    else:
        return Exception("requested direction occupied or invalid")

def move(direction):
    if direction == "down":
        try:
            if movecheck("down"):
                gentetramino("white")
                gamestorage.currenty -= 1
                gentetramino()
            else:
                print(direction+" check failure")
        except:
            gamestorage.orientation = 0
            gamestorage.currentx = 5
            gamestorage.currenty = 20
            gamestorage.currenttetramino = gamestorage.tetraminoes[random.randint(0, 4)]
            lineclear()
            gentetramino()
            print("uh oh its back up to the top 4 you")


    if direction == "left":
        if movecheck("left"):
            gentetramino("white")
            gamestorage.currentx -= 1
            gentetramino()
        else:
            print(direction+" check failure")
    if direction == "right":
        if movecheck("right"):
            gentetramino("white")
            gamestorage.currentx += 1
            gentetramino()
        else:
            print(direction+" check failure")


def turn(direction):
    if direction == "left":
        if turncheck("left"):
            gentetramino("white")
            if gamestorage.orientation == 3:
                gamestorage.orientation = 0
            else:
                gamestorage.orientation += 1
            gentetramino()
        else:
            print(direction + " check failure")
    elif direction == "right":
        if turncheck("right"):
            gentetramino("white")
            if gamestorage.orientation == 0:
                gamestorage.orientation = 3
            else:
                gamestorage.orientation -= 1
            gentetramino()
        else:
            print(direction + " check failure")

def lineclear():
    temp = []
    for y in range(0, 21):
        w = 0
        for x in range(0, 10):
            if eval("ct.x" + str(x) + "y" + str(y) + ".cget('bg')") != "white":
                print("woohoo")
            else:
                print("awe")
                w = 1
        if w == 0:
            temp.append(y)
            continue
        for k in temp:
            temp.pop(-1)
            for x in range(0, 11):
                exec("ct." + ct.coordconstructor(x, k) + ".config(bg = 'white')")
            for i in range(k, 21):
                try:
                    for j in range(0, 11):
                        a = "ct." + ct.coordconstructor(j, i)
                        b = eval("ct." + ct.coordconstructor(j, i + 1) + ".cget('bg')")
                        eval(a + ".config(bg='" + b + "')")
                except:
                    break
            gamestorage.score += 500
            print(gamestorage.score)


def keypress(event):
    global time
    if event.keysym == "d":
        time = 0
        print("e")
        move("right")
    elif event.keysym == "s":
        time = 0
        print("s")
        move("down")
    elif event.keysym == "a":
        time = 0
        print("w")
        move("left")
    elif event.keysym == "r":
        print("r")
        turn("right")

debugleft = tkinter.Button(text="left", command=lambda: move("left"))
debugright = tkinter.Button(text="right", command=lambda: move("right"))
debugdown = tkinter.Button(text="down", command=lambda: move("down"))
debuggentetramino = tkinter.Button(text="gentet", command=lambda: exec("gentetramino('white'); gamestorage.orientation = 0; gamestorage.currentx = 5; gamestorage.currenty = 20;gamestorage.currenttetramino=gamestorage.tetraminoes[random.randint(0, 4)]; gentetramino()"))
debugturnleft = tkinter.Button(text="turnleft", command=lambda: exec("turn('left'), print(gamestorage.orientation)"))
debugturnright = tkinter.Button(text="turnright", command=lambda: exec("turn('right'), print(gamestorage.orientation)"))
debuglineclear = tkinter.Button(text="lineclear", command=lambda: exec("lineclear()"))
debugleft.grid(row=1, column=21)
debugright.grid(row=2, column=21)
debugturnleft.grid(row=3, column=21)
debugturnright.grid(row=4, column=21)
debugdown.grid(row=5, column=21)
debuggentetramino.grid(row=6, column=21)
debuglineclear.grid(row=7, column=21)
time = 0
def loop():
    global time
    if time == 10:
        move("down")
        time = 0
    else:
        time += 1
    window.after(100, loop)
loop()
window.bind("<Key>", keypress)
window.mainloop()