import tkinter, coordtools as ct

window = tkinter.Tk()
ct.gencoords(20, 20)

class paddle1:
    a="#"
    b="#"
    c="#"
    order=["a", "b", "c"]
    x = 0
    y = 0
class paddle2:
    a="#"
    b="#"
    c="#"
    order=["a", "b", "c"]
    x = 19
    y = 18
class ball:
    a="#"
    order=["a",]
    x=10
    y=10
    hdirection=1
    vdirection=1
def keypress(event):
    if event.keysym == "w":
        ct.move(paddle1, x=0, y=1)
    elif event.keysym == "s":
        ct.move(paddle1, x=0, y=-1)

def pongloop():
    for i in ct.coordlist:
        eval("ct."+i)["bg"] = "black"
        eval("ct." + i)["textvariable"] = ""
    ct.drawsprite(paddle1, color="white")
    print(paddle1.x, paddle1.y)
    ct.drawsprite(paddle2, color="white")
    if not ct.spacecheck(ball, x=ball.hdirection):
        ball.hdirection *= -1
    elif not ct.spacecheck(ball, y=ball.vdirection):
        ball.vdirection *= -1
    print(ct.spacecheck(ball, y=ball.vdirection))
    print(ball.vdirection)
    ct.move(ball, x=ball.hdirection, y=ball.vdirection)
    ct.drawsprite(ball, color="white")
    window.after(100, pongloop)

window.bind("<Key>", keypress)
window.after(100, pongloop)
window.mainloop()