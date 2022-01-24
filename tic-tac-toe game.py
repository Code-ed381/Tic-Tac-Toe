import tkinter
from tkinter import *
from tkinter.constants import DISABLED, NORMAL

window = tkinter.Tk()
window.geometry('300x350')
window.title("Xs AND Os")
window.configure(bg="#FFE135")

def changeStateOne():
        xButton['state'] = tkinter.DISABLED
        xButton['bg'] = 'black'
        xButton['fg'] = 'white'
        oButton['state'] = tkinter.NORMAL
        oButton['bg'] = 'white'
        oButton['fg'] = 'black'

def changeStateTwo():
        xButton['state'] = tkinter.NORMAL
        xButton['bg'] = 'white'
        xButton['fg'] = 'black'
        oButton['state'] = tkinter.DISABLED
        oButton['bg'] = 'black'
        oButton['fg'] = 'white'


def boxOne(event):
    if xButton['state'] == tkinter.NORMAL:
        btOne = box1.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box1.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        btOne = box1.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box1.unbind('<Button-1>')

def boxTwo(event):
    if xButton['state'] == tkinter.NORMAL:
        box2.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box2.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        box2.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box2.unbind('<Button-1>')

def boxThree(event):
    if xButton['state'] == tkinter.NORMAL:
        box3.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box3.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        box3.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box3.unbind('<Button-1>')

def boxFour(event):
    if xButton['state'] == tkinter.NORMAL:
        box4.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box4.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        box4.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box4.unbind('<Button-1>')

def boxFive(event):
    if xButton['state'] == tkinter.NORMAL:
        box5.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box5.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        box5.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box5.unbind('<Button-1>')

def boxSix(event):
    if xButton['state'] == tkinter.NORMAL:
        box6.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box6.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        box6.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box6.unbind('<Button-1>')

def boxSeven(event):
    if xButton['state'] == tkinter.NORMAL:
        box7.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box7.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        box7.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box7.unbind('<Button-1>')

def boxEight(event):
    if xButton['state'] == tkinter.NORMAL:
        box8.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box8.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        box8.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box8.unbind('<Button-1>')

def boxNine(event):
    if xButton['state'] == tkinter.NORMAL:
        box9.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box9.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        box9.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box9.unbind('<Button-1>')
    

canvas = tkinter.Canvas(window,bg="white",highlightthickness=0)
canvas.place(x=10,y=20,width=270)
canvas.create_line(90,250,90,20, fill="green", width=3)
canvas.create_line(180,250,180,20, fill="green", width=3)
canvas.create_line(20,90,250,90, fill="green", width=3)
canvas.create_line(20,180,250,180, fill="green", width=3)

box1 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box1.bind("<Button-1>",boxOne)
box1.place(x=20,y=30)

box2 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box2.bind("<Button-1>",boxTwo)
box2.place(x=108,y=30)

box3 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box3.bind("<Button-1>", boxThree)
box3.place(x=196,y=30)

box4 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box4.bind("<Button-1>", boxFour)
box4.place(x=20,y=120)

box5 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box5.bind("<Button-1>", boxFive)
box5.place(x=108,y=120)

box6 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box6.bind("<Button-1>", boxSix)
box6.place(x=196,y=120)

box7 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box7.bind("<Button-1>", boxSeven)
box7.place(x=20,y=205)

box8 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box8.bind("<Button-1>", boxEight)
box8.place(x=108,y=205)

box9 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box9.bind("<Button-1>", boxNine)
box9.place(x=196,y=205)

xButton = tkinter.Button(window,text="X",font="Calibri 14",fg="black",bg="white", state=NORMAL)
xButton.place(x=45,y=300,width=100)
oButton = tkinter.Button(window,text="O",font="Calibri 14",fg="white",bg="black", state=DISABLED)
oButton.place(x=145,y=300,width=100)

window.mainloop()
