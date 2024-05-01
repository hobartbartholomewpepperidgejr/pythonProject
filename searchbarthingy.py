import tkinter, webbrowser, requests
from termcolors import *

def funcclear():
    entry.delete(0, 'end')
def funcsubmit():
    print(tcolor("green")+entry.get())
    funcclear()
def funcsearch():
    try:
        x = requests.head(entry.get())
        print(x.status_code)
        if x.status_code == 200:
            print(tcolor("green")+"connecting..")
            webbrowser.open(entry.get())
    except:
        print(tcolor("red")+"error (invalid url)")
        funcclear()

window = tkinter.Tk()

img=tkinter.PhotoImage(file="C:/Users/cb27228/Pictures/Screenshots/Screenshot 2024-01-12 141317.png")

search=tkinter.Button(text="search",
                      command=funcsearch)
clear=tkinter.Button(text="clear",
                     command=funcclear)
submit=tkinter.Button(text="submit",
                      command=funcsubmit)
entry=tkinter.Entry()

errorbox=tkinter.Message(text='no errors')

entry.grid(column=0, columnspan=8, sticky='nesw')
search.grid(row=0, column=8, sticky='nesw')
clear.grid(row=0, column=9, sticky='nesw')
submit.grid(row=0, column=10, sticky='nesw')

for i in range(10):
    window.grid_columnconfigure(i, weight=1)
window.grid_rowconfigure(0, weight=1)

window.title("the best bootleg-not-even-a-real-browser-its-actually-more-of-a-middleman-than-anything you'll ever see")
window.iconphoto('self', img)

window.mainloop()