import tkinter

def doireallyneedtodothis():
    cookiestats["cookies"] += 1
    print(cookiestats["cookies"])

cookiestats = {
    "cookies": 0,
    "cps": 0
}

window = tkinter.Tk()
window.geometry("300x300")
dumbstuff = tkinter.Button(text="wowie",
                          command=doireallyneedtodothis,
                          compound='bottom')

dumbstuff.grid(row=0, column=0, sticky='nesw')

window.mainloop()