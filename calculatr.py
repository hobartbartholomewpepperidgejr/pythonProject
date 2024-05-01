import tkinter
values=[]
global ab
ab = ""
def youshouldsubscriptyourselfNOW(a):
    values.append(a)
    global ab   # make var ab usable
    for i in values:
        print(i, end= "")   # print the current numbers + operators 2 the console
    ab = str(ab) + str(i)   # update ab to be in line with the list
    label.config(text=ab)   # set the input bar to the list's contents
    print("")   # newline
    if len(values) >= 11:   # keep the bar from going off the window (i dont wanna fix it)
        clear("values")
        print("too long!")
        label.config(text="too long >11")
def clear(a):
    if a == "values":
        values.clear()
        global ab
        ab = ""
        label.config(text="")
    elif a == "output":
        output.config(text="")
def calculate():
    try:
        print(eval(ab))
        output.config(text=eval(ab))
        clear("values")
    except:
        print("no thingies")
        clear("output")
        clear("values")


window=tkinter.Tk()
# this hurts so much to look at (please collapse it for the love of god)
if True:
    label = tkinter.Label(text="")
    label.grid(row=0, column=3, columnspan=5, sticky="w")
    placeholder = tkinter.Label(text="      ")
    placeholder.grid(row=1, column=6)
    output = tkinter.Message(text="")
    output.grid(row=1, column=5, rowspan=3, columnspan=2, sticky="nesw")
    button7 = tkinter.Button(text="7", command=lambda: youshouldsubscriptyourselfNOW(7))
    button7.grid(column=0, row=0)
    button8 = tkinter.Button(text="8", command=lambda: youshouldsubscriptyourselfNOW(8))
    button8.grid(column=1, row=0)
    button9 = tkinter.Button(text="9", command=lambda: youshouldsubscriptyourselfNOW(9))
    button9.grid(column=2, row=0)
    button4 = tkinter.Button(text="4", command=lambda: youshouldsubscriptyourselfNOW(4))
    button4.grid(column=0, row=1)
    button5 = tkinter.Button(text="5", command=lambda: youshouldsubscriptyourselfNOW(5))
    button5.grid(column=1, row=1)
    button6 = tkinter.Button(text="6", command=lambda: youshouldsubscriptyourselfNOW(6))
    button6.grid(column=2, row=1)
    button1 = tkinter.Button(text="1", command=lambda: youshouldsubscriptyourselfNOW(1))
    button1.grid(column=0, row=2)
    button2 = tkinter.Button(text="2", command=lambda: youshouldsubscriptyourselfNOW(2))
    button2.grid(column=1, row=2)
    button3 = tkinter.Button(text="3", command=lambda: youshouldsubscriptyourselfNOW(3))
    button3.grid(column=2, row=2)
    button0 = tkinter.Button(text="0", command=lambda: youshouldsubscriptyourselfNOW(0))
    button0.grid(column=0, row=3)
    buttonnaught = tkinter.Button(text=".", command=lambda: youshouldsubscriptyourselfNOW("."))
    buttonnaught.grid(column=1, row=3, columnspan=2, sticky="nesw")
    buttonplus = tkinter.Button(text="+", command=lambda: youshouldsubscriptyourselfNOW("+"))
    buttonplus.grid(column=3, row=1, sticky="nesw")
    buttonminus = tkinter.Button(text="-", command=lambda: youshouldsubscriptyourselfNOW("-"))
    buttonminus.grid(column=3, row=2, sticky="nesw")
    buttontimes = tkinter.Button(text="*", command=lambda: youshouldsubscriptyourselfNOW("*"))
    buttontimes.grid(column=4, row=1, sticky="nesw")
    buttondivided = tkinter.Button(text="/", command=lambda: youshouldsubscriptyourselfNOW("/"))
    buttondivided.grid(column=4, row=2, sticky="nesw")
    buttoncalculate = tkinter.Button(text="=", command=calculate)
    buttoncalculate.grid(column=3, columnspan=2, sticky="nesw", row=3)
    window.geometry("125x102")
    window.resizable(width=False, height=False)
window.mainloop()