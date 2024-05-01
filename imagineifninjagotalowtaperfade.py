import tkinter, random, coordtools
window = tkinter.Tk()
window.geometry("620x620")
blank = tkinter.PhotoImage(file="H:\wad.png")
applecoords = "x15y15"
D = 0
speed = 100
delay = 0
buffer=[]
snake={
    "heading": 0,
    "x": 15,
    "y": 15,
    "length": 2,
    "score": 0
}

print("wasd to control your direction (probably dont press two keys at once too fast) (can't be bothered to implement an input buffer) (yet)")
print("shift to speed up (you cant turn while sped up)")

for width in range(0, 31):
    for height in range(0, 31):
        exec("x"+str(width)+"y"+str(height)+" = tkinter.Label(text='', bg='white', image=blank)")
        exec("x"+str(width)+"y"+str(height)+".grid(column="+str(width)+", row="+str(height)+", sticky='nesw')")

def keypress(event):
    if event.keysym == "w" and not snake["heading"] == 3:
        print("n")
        snake["heading"] = 1
    elif event.keysym == "d" and not snake["heading"] == 4:
        print("e")
        snake["heading"] = 2
    elif event.keysym == "s" and not snake["heading"] == 1:
        print("s")
        snake["heading"] = 3
    elif event.keysym == "a" and not snake["heading"] == 2:
        print("w")
        snake["heading"] = 4
    global speed
    if event.keysym == "Shift_L":
        speed = 25
    else:
        speed = 100

def applecoordpicker():
    global applecoords
    exec(applecoords+".config(bg='green')")
    applecoords = coordtools.coordconstructor(random.randint(1, 30), random.randint(1, 30))
    exec(applecoords+".config(bg='red')")

#cycling without a bike
def snakeloop():
    coords = coordtools.coordconstructor(snake["x"], snake["y"])
    global applecoords
    life = snake["length"] * 10 # convert 2 seconds
    for i in buffer:
        if coords == i and len(buffer) > 2:
            print("imagine dying loser")
            print("skill issue: "+str(snake["score"]))
            exit()
    try:
        exec(str(buffer[0])+".config(bg='white')")
        buffer.pop(0)
    except:
        print(">:]")
    if snake.get("heading") == 1:
        snake["y"] -= 1
    elif snake.get("heading") == 2:
        snake["x"] += 1
    elif snake.get("heading") == 3:
        snake["y"] += 1
    elif snake.get("heading") == 4:
        snake["x"] -= 1
    #print(snake["heading"], snake["x"], snake["y"])
    try:
        exec("x"+str(snake["x"])+"y"+str(snake["y"])+".config(bg='green')")
    except:
        print("imagine dying loser")
        print("skill issue: "+str(snake["score"]))
        exit()
    buffer.append(coords)
    if coords == applecoords:
        buffer.append(coords)
        applecoordpicker()
        snake["score"] += 100
    #print(buffer)
    snake["score"] -= 1
    window.after(speed, snakeloop)

#window n binding
window.bind("<Key>", keypress)
window.bind(snakeloop)
window.bind(applecoordpicker)
window.after(0, snakeloop)
window.mainloop()


