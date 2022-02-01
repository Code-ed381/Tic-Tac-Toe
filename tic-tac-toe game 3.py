import tkinter
from tkinter import *
from tkinter import Menu
"""from tkinter.constants import DISABLED, NORMAL"""


window = tkinter.Tk()
window.geometry('300x400')
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

btOne = ''
btTwo = ''
btThree = ''
btFour = ''
btFive = ''
btSix = ''
btSeven = ''
btEight = ''
btNine = ''

def boxOne(event):
    global btOne
    if xButton['state'] == NORMAL:
        btOne = box1.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box1.unbind('<Button-1>')
    elif xButton['state'] == DISABLED:
        btOne = box1.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box1.unbind('<Button-1>')
    win()

def boxTwo(event):
    global btTwo
    if xButton['state'] == tkinter.NORMAL:
        btTwo = box2.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box2.unbind('<Button-1>')        
    elif xButton['state'] == tkinter.DISABLED:
        btTwo = box2.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box2.unbind('<Button-1>')
    win()

def boxThree(event):
    global btThree
    if xButton['state'] == tkinter.NORMAL:
        btThree = box3.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box3.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        btThree = box3.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box3.unbind('<Button-1>')
    win()

def boxFour(event):
    global btFour
    if xButton['state'] == tkinter.NORMAL:
        btFour = box4.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box4.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        btFour = box4.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box4.unbind('<Button-1>')
    win()

def boxFive(event):
    global btFive
    if xButton['state'] == tkinter.NORMAL:
        btFive = box5.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box5.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        btFive = box5.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box5.unbind('<Button-1>')
    win()

def boxSix(event):
    global btSix
    if xButton['state'] == tkinter.NORMAL:
        btSix = box6.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box6.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        btSix = box6.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box6.unbind('<Button-1>')
    win()

def boxSeven(event):
    global btSeven
    if xButton['state'] == tkinter.NORMAL:
        btSeven = box7.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box7.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        btSeven = box7.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box7.unbind('<Button-1>')
    win()

def boxEight(event):
    global btEight
    if xButton['state'] == tkinter.NORMAL:
        btEight = box8.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box8.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        btEight = box8.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box8.unbind('<Button-1>')
    win()

def boxNine(event):
    global btNine
    if xButton['state'] == tkinter.NORMAL:
        btNine = box9.create_text(40,40,text="x",font="Arial 72")
        changeStateOne()
        box9.unbind('<Button-1>')
    elif xButton['state'] == tkinter.DISABLED:
        btNine = box9.create_text(40,40,text="o",font="Arial 72")
        changeStateTwo()
        box9.unbind('<Button-1>')
    win()

def Help():
    howToTxt = " You probably already know how to play Tic-Tac-Toe. \nIt's a really simple game, right? That's what most people think. \nBut if you really wrap your brain around it, you'll discover that \nTic-Tac-Toe isn't quite as simple as you think! \nTic-Tac -Toe (along with a lot of other games) involves looking ahead and \ntrying to figure out what the person playing against you might do next. "
    rulesTxt = " 1. The game is played on a grid that's 3 squares by 3 squares.\n\n 2. You are X, your opponent is O.\n Players take turns putting their marks in empty squares.\n\n 3. The first player to get 3 of her marks in a row \n(up, down, across, or diagonally) is the winner. \n\n4. When all 9 squares are full, the game is over. \nIf no player has 3 marks in a row, the game ends in a tie. "
    help = Toplevel(master=None)
    help.title("Help")
    help.geometry('450x400')
    help.config(bg='white')

    howToPlay = tkinter.Label(help, text='How to play', bg='white', font='Arial 14')
    howToPlay.pack()
    howTo = tkinter.Label(help, text=howToTxt, bg='white', font='Arial 10')
    howTo.pack()

    rules = tkinter.Label(help, text='\nRules of the game', bg='white', font='Arial 14')
    rules.pack()
    rulesText = tkinter.Label(help, text=rulesTxt, bg='white', font='Arial 10')
    rulesText.pack()

def Restart(newTopLevel):
    changeStateTwo()

    box1.delete('all')
    box2.delete('all')
    box3.delete('all')
    box4.delete('all')
    box5.delete('all')
    box6.delete('all')
    box7.delete('all')
    box8.delete('all')
    box9.delete('all')

    box1.bind('<Button-1>', boxOne)
    box2.bind('<Button-1>', boxTwo)
    box3.bind('<Button-1>', boxThree)
    box4.bind('<Button-1>', boxFour)
    box5.bind('<Button-1>', boxFive)
    box6.bind('<Button-1>', boxSix)
    box7.bind('<Button-1>', boxSeven)
    box8.bind('<Button-1>', boxEight)
    box9.bind('<Button-1>', boxNine)

    newTopLevel.destroy()

def MenuNewGame():
    changeStateTwo()

    box1.delete('all')
    box2.delete('all')
    box3.delete('all')
    box4.delete('all')
    box5.delete('all')
    box6.delete('all')
    box7.delete('all')
    box8.delete('all')
    box9.delete('all')

    box1.bind('<Button-1>', boxOne)
    box2.bind('<Button-1>', boxTwo)
    box3.bind('<Button-1>', boxThree)
    box4.bind('<Button-1>', boxFour)
    box5.bind('<Button-1>', boxFive)
    box6.bind('<Button-1>', boxSix)
    box7.bind('<Button-1>', boxSeven)
    box8.bind('<Button-1>', boxEight)
    box9.bind('<Button-1>', boxNine)
 
def Winner(winner):
    if winner == 'player1':
        newwindow = Toplevel(master=None)
        newwindow.title('Player One Wins')
        newwindow.geometry('320x200')
        newwindow.config(bg='white')

        winMessage = Label(newwindow, text='Player One Won this game', bg='white', font='Calibri 14')
        winMessage.place(x=40, y=25)
        newGame = Button(newwindow, text='New game',width='10', font='Arial 14',image=newGame_Btn, command=lambda: Restart(newwindow))
        newGame.place(x=100, y=65)
        exit = Button(newwindow, text='Exit',width='10', font='Arial 14', command=lambda: window.destroy())
        exit.place(x=100, y=105)
        #newGame_Btn.show()

    if winner == 'player2':
        newwindow = Toplevel(master=None)
        newwindow.title('Player One Wins')
        newwindow.geometry('320x200')
        newwindow.config(bg='white')

        winMessage = Label(newwindow, text='Player Two Won this game', bg='white', font='Calibri 14')
        winMessage.place(x=40, y=25)
        newGame = Button(newwindow, text='New game',width='10', font='Arial 14', command=lambda: Restart(newwindow))
        newGame.place(x=100, y=65)
        exit = Button(newwindow, text='Exit',width='10', font='Arial 14', command=lambda: window.destroy())
        exit.place(x=100, y=105)
    
    if winner == 'draw':
        newwindow = Toplevel(master=None)
        newwindow.title('Player One Wins')
        newwindow.geometry('320x200')
        newwindow.config(bg='white')

        winMessage = Label(newwindow, text="It's a tie", bg='white', font='Calibri 14')
        winMessage.place(x=40, y=25)
        newGame = Button(newwindow, text='New game',width='10', font='Arial 14', command=lambda: Restart(newwindow))
        newGame.place(x=100, y=65)
        exit = Button(newwindow, text='Exit',width='10', font='Arial 14', command=lambda: window.destroy())
        exit.place(x=100, y=105)

def win():
    if box1.itemcget(btOne, 'text') == 'x' and box2.itemcget(btTwo, 'text') == 'x' and box3.itemcget(btThree, 'text') == 'x':
        winner = 'player1'
        Winner(winner)
    elif box1.itemcget(btOne, 'text') == 'o' and box2.itemcget(btTwo, 'text') == 'o' and box3.itemcget(btThree, 'text') == 'o':
        winner = 'player2'
        Winner(winner)
    elif box4.itemcget(btFour, 'text') == 'x' and box5.itemcget(btFive, 'text') == 'x' and box6.itemcget(btSix, 'text') == 'x':
        winner = 'player1'
        Winner(winner)
    elif box4.itemcget(btFour, 'text') == 'o' and box5.itemcget(btFive, 'text') == 'o' and box6.itemcget(btSix, 'text') == 'o':
        winner = 'player2'
        Winner(winner)
    elif box7.itemcget(btSeven, 'text') == 'x' and box8.itemcget(btEight, 'text') == 'x' and box9.itemcget(btNine, 'text') == 'x':
        winner = 'player1'
        Winner(winner)
    elif box7.itemcget(btSeven, 'text') == 'o' and box8.itemcget(btEight, 'text') == 'o' and box9.itemcget(btNine, 'text') == 'o':
        winner = 'player2'
        Winner(winner)
    elif box1.itemcget(btOne, 'text') == 'x' and box4.itemcget(btFour, 'text') == 'x' and box7.itemcget(btSeven, 'text') == 'x':
        winner = 'player1'
        Winner(winner)
    elif box1.itemcget(btOne, 'text') == 'o' and box4.itemcget(btFour, 'text') == 'o' and box7.itemcget(btSeven, 'text') == 'o':
        winner = 'player2'
        Winner(winner)
    elif box2.itemcget(btTwo, 'text') == 'x' and box5.itemcget(btFive, 'text') == 'x' and box8.itemcget(btEight, 'text') == 'x':
        winner = 'player1'
        Winner(winner)
    elif box2.itemcget(btTwo, 'text') == 'o' and box5.itemcget(btFive, 'text') == 'o' and box8.itemcget(btEight, 'text') == 'o':
        winner = 'player2'
        Winner(winner)
    elif box3.itemcget(btThree, 'text') == 'x' and box6.itemcget(btSix, 'text') == 'x' and box9.itemcget(btNine, 'text') == 'x':
        winner = 'player1'
        Winner(winner)
    elif box3.itemcget(btThree, 'text') == 'o' and box6.itemcget(btSix, 'text') == 'o' and box9.itemcget(btNine, 'text') == 'o':
        winner = 'player2'
        Winner(winner)
    elif box1.itemcget(btOne, 'text') == 'x' and box5.itemcget(btFive, 'text') == 'x' and box9.itemcget(btNine, 'text') == 'x':
        winner = 'player1'
        Winner(winner)
    elif box1.itemcget(btOne, 'text') == 'o' and box5.itemcget(btFive, 'text') == 'o' and box9.itemcget(btNine, 'text') == 'o':
        winner = 'player2'
        Winner(winner)
    elif box3.itemcget(btThree, 'text') == 'x' and box5.itemcget(btFive, 'text') == 'x' and box7.itemcget(btSeven, 'text') == 'x':
        winner = 'player1'
        Winner(winner)
    elif box3.itemcget(btThree, 'text') == 'o' and box5.itemcget(btFive, 'text') == 'o' and box7.itemcget(btSeven, 'text') == 'o':
        winner = 'player2'
        Winner(winner)
    elif box1.itemcget(btOne, 'text') != '' and box2.itemcget(btTwo, 'text') != '' and box3.itemcget(btThree, 'text') != '' and box4.itemcget(btFour, 'text') != '' and box5.itemcget(btFive, 'text') != '' and box6.itemcget(btSix, 'text') != '' and box7.itemcget(btSeven, 'text') != '' and box8.itemcget(btEight, 'text') != '' and box9.itemcget(btNine, 'text') != '':
        winner = 'draw'
        Winner(winner)

menu_widget = Menu(window)
window.config(menu=menu_widget)

submenu_widget = Menu(menu_widget, tearoff=FALSE)
submenu_widget.add_command(label="New game", command=MenuNewGame)
submenu_widget.add_command(label="Exit", command=lambda: window.destroy())

menu_widget.add_cascade(label="Options", menu=submenu_widget)
menu_widget.add_command(label="Help", command=Help)

canvas = tkinter.Canvas(window,bg="white",highlightthickness=0)
canvas.place(x=10,y=70,width=270)
canvas.create_line(90,250,90,20, fill="green", width=3)
canvas.create_line(180,250,180,20, fill="green", width=3)
canvas.create_line(20,90,250,90, fill="green", width=3)
canvas.create_line(20,180,250,180, fill="green", width=3)

box1 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box1.bind("<Button-1>",boxOne)
box1.place(x=20,y=80)

box2 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box2.bind("<Button-1>",boxTwo)
box2.place(x=108,y=80)

box3 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box3.bind("<Button-1>", boxThree)
box3.place(x=196,y=80)

box4 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box4.bind("<Button-1>", boxFour)
box4.place(x=20,y=168)

box5 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box5.bind("<Button-1>", boxFive)
box5.place(x=108,y=168)

box6 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box6.bind("<Button-1>", boxSix)
box6.place(x=196,y=168)

box7 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box7.bind("<Button-1>", boxSeven)
box7.place(x=20,y=255)

box8 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box8.bind("<Button-1>", boxEight)
box8.place(x=108,y=255)

box9 = tkinter.Canvas(window,width=75,height=75,bg="white",highlightthickness=0)
box9.bind("<Button-1>", boxNine)
box9.place(x=196,y=255)

xButton = tkinter.Button(window,text="X",font="Calibri 14",fg="black",bg="white", state=NORMAL)
xButton.place(x=45,y=350,width=100)
oButton = tkinter.Button(window,text="O",font="Calibri 14",fg="white",bg="black", state=DISABLED)
oButton.place(x=145,y=350,width=100)

window.mainloop()

