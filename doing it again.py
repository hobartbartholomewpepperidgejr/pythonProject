import tkinter
window = tkinter.Tk()
topbar=tkinter.Label(text="enter your info", font="arial 25")
topbar.grid(row=0, column=0, columnspan=3, sticky="we")
for i in range(5):
    exec("entry"+str(i)+"=tkinter.Entry()")
    exec("entry"+str(i)+".grid(row="+str(i+1)+", column=1, padx=3)")
text=("first name", "last name", "email", "phone", "address")
bgs=('#FF474C', '#90EE90', '#ADD8E6', 'white', '#f08080')
for i in range(5):
    exec("label"+str(i)+"=tkinter.Label(text=text[i], bg=bgs[i])")
    exec("label"+str(i)+".grid(row="+str(i+1)+", column=0, padx=3)")
def youidiot():
    exec('for i in range(5): exec("print(entry"+str(i)+".get())")')
submit=tkinter.Button(text="submit", command=youidiot)
submit.grid(row=6, column=0, columnspan=2)
window.mainloop()