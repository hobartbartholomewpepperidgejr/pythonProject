import tkinter, termcolors

# 1
window = tkinter.Tk()
window.title("a title")
window.geometry("500x500")
window.config(bg="grey")
# 2
labelle = tkinter.Label(text="wowie", height=5, width=15, bg="white", fg="black")

# 3
buttonne = tkinter.Button(text="wowza", height=5, width=15, bg="white", fg="black")

# 4
textBOX = tkinter.Text(height=5, width=15, bg="white", fg="black")

#5
textinput = tkinter.Entry(width=15)

#6
messagething = tkinter.Message(text="what even is this", bg="white", fg="black")

#7
checkBOX = tkinter.Checkbutton(text="yeah", width="10", bg="white", fg="black")

#the END (load order)
textBOX.pack()
buttonne.pack()
labelle.pack()
checkBOX.pack()
textinput.pack()
messagething.pack()


window.mainloop()