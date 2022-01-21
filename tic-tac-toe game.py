import tkinter
from tkinter import *
from tkinter.constants import DISABLED, NORMAL

def leftclick(event):
    box1.create_text(40,40,text="x",font="Arial 72")
    xButton['state'] = tkinter.DISABLED
    xButton['bg'] = 'black'
    oButton['state'] = tkinter.NORMAL
    oButton['bg'] = 'white'
    oButton['fg'] = 'black'
def leftclick2(event):
    box2.create_text(40,40,text="o",font="Arial 72")
    xButton['state'] = tkinter.NORMAL
    xButton['bg'] = 'white'
    xButton['fg'] = 'black'
    oButton['state'] = tkinter.DISABLED
    oButton['bg'] = 'black'

    
window = tkinter.Tk()
window.geometry('300x350')
window.title("Xs AND Os")
window.configure(bg="pink")

canvas = tkinter.Canvas(window,bg="white",highlightthickness=0)
canvas.place(x=10,y=20,width=270)
canvas.create_line(90,250,90,20, fill="green", width=3)
canvas.create_line(180,250,180,20, fill="green", width=3)
canvas.create_line(20,90,250,90, fill="green", width=3)
canvas.create_line(20,180,250,180, fill="green", width=3)

'''myFrame1 = Frame(window,width=75,height=75)
myFrame1.bind("<Button-1>",leftclick)
myFrame1.place(x=20,y=30)'''

box1 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box1.bind("<Button-1>",leftclick)
box1.place(x=20,y=30)

box2 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box2.bind("<Button-1>",leftclick2)
box2.place(x=108,y=30)

box3 = tkinter.Canvas(window,width=75,height=75,highlightthickness=0)
box3.bind("<Button-1>",leftclick)
box3.place(x=196,y=30)

box4 = tkinter.Canvas(window,width=75,height=75,highlightthickness=0)
box4.bind("<Button-1>",leftclick)
box4.place(x=20,y=120)

box5 = tkinter.Canvas(window,width=75,height=75,highlightthickness=0)
box5.bind("<Button-1>",leftclick)
box5.place(x=108,y=120)

box6 = tkinter.Canvas(window,width=75,height=75,highlightthickness=0)
box6.bind("<Button-1>",leftclick)
box6.place(x=196,y=120)

box7 = tkinter.Canvas(window,width=75,height=75,highlightthickness=0)
box7.bind("<Button-1>",leftclick)
box7.place(x=20,y=205)

box8 = tkinter.Canvas(window,width=75,height=75,highlightthickness=0)
box8.bind("<Button-1>",leftclick)
box8.place(x=108,y=205)

box9 = tkinter.Canvas(window,width=75,height=75,highlightthickness=0)
box9.bind("<Button-1>",leftclick)
box9.place(x=196,y=205)

xClick = canvas.postscript
xButton = tkinter.Button(window,text="X",font="Calibri 14",fg="black",bg="white", state=NORMAL)
xButton.place(x=45,y=300,width=100)
oButton = tkinter.Button(window,text="O",font="Calibri 14",fg="white",bg="black", state=DISABLED)
oButton.place(x=145,y=300,width=100)



window.mainloop()
