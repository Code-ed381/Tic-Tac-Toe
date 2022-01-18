import tkinter
from tkinter import *
from tkinter.constants import DISABLED, NORMAL
from tkinter import messagebox

root = Tk()

root.geometry('355x400')

root.title('Tic-Tac-Toe')

root.configure(bg='#36454F')

menu_widget = tkinter.Menu(root)

submenu_widget = tkinter.Menu(menu_widget, tearoff=False)

menu_widget.add_cascade(label="Options")

menu_widget.add_command(label="Help")

root.config(menu = menu_widget)





def changeState():
    if (playerOneBtn['state'] == tkinter.NORMAL) :
        playerOneBtn['state'] = tkinter.DISABLED
        playerOneBtn['bg'] = 'red'
        playerOneBtn['fg'] = 'black'
    else:
        playerOneBtn['state'] = tkinter.NORMAL
        playerOneBtn['bg'] = 'green'
        playerOneBtn['fg'] = 'white'

    if (playerTwoBtn['state'] == tkinter.DISABLED):
        playerTwoBtn['state'] = tkinter.NORMAL
        playerTwoBtn['bg'] = 'green'
        playerTwoBtn['fg'] = 'white'
    else:
        playerTwoBtn['state'] = tkinter.DISABLED
        playerTwoBtn['bg'] = 'red'
        playerTwoBtn['fg'] = 'black'

playerOneBtn = tkinter.Button(root, text='Player 1 (X)', fg='white', bg='green', font="Arial 10", state=NORMAL)
playerOneBtn.place(x=80, y=40)


playerTwoBtn = tkinter.Button(root, text='Player 2 (O)', fg='black', bg='red',font="Arial 10", state=DISABLED)
playerTwoBtn.place(x=185, y=40)


row1col1 = StringVar()
row1col2 = StringVar()
row1col3 = StringVar()
row2col1 = StringVar()
row2col2 = StringVar()
row2col3 = StringVar()
row3col1 = StringVar()
row3col2 = StringVar()
row3col3 = StringVar()



def Restart(winMessageFxn):
    r1c1['state'] = tkinter.NORMAL
    r1c2['state'] = tkinter.NORMAL
    r1c3['state'] = tkinter.NORMAL
    r2c1['state'] = tkinter.NORMAL
    r2c2['state'] = tkinter.NORMAL
    r2c3['state'] = tkinter.NORMAL
    r3c1['state'] = tkinter.NORMAL
    r3c2['state'] = tkinter.NORMAL
    r3c3['state'] = tkinter.NORMAL

    row1col1.set('')
    row1col2.set('')
    row1col3.set('')
    row2col1.set('')
    row2col2.set('')
    row2col3.set('')
    row3col1.set('')
    row3col2.set('')
    row3col3.set('')

    winMessageFxn.destroy()


    changeState()
    
    

def Winner(winner):
    if winner == 'Player 1':
        winMessage = Toplevel(master=None)
        winMessage.title("Winner")
        winMessage.geometry('300x200')
        winMessage.config(bg='white')

        winnerText = tkinter.Label(winMessage,text='Player one won the game', bg='white',font='Calibri 12')
        winnerText.place(x=42, y=30)
        newgame = tkinter.Button(winMessage, text='New game', font='Arial 12', command= lambda : Restart(winMessage))
        newgame.place(x=100, y=65)
        newgame = tkinter.Button(winMessage, text='Exit', font='Arial 12', command = lambda: root.destroy())
        newgame.place(x=127, y=105)

    else:
        winMessage = Toplevel(master=None)
        winMessage.title("Winner")
        winMessage.geometry('300x200')
        winMessage.config(bg='white')

        winnerText = tkinter.Label(winMessage,text='Player two won the game', bg='white', font='Calibri 12')
        winnerText.place(x=42, y=30)
        newgame = tkinter.Button(winMessage, text='New game', font='Arial 12', command= lambda : Restart(winMessage))
        newgame.place(x=100, y=65)
        newgame = tkinter.Button(winMessage, text='Exit', font='Arial 12', command = lambda: root.destroy())
        newgame.place(x=127, y=105)


def btnOneCmd(x, y, z):
    if playerOneBtn['state'] == tkinter.NORMAL:
        row1col1.set(x)
        changeState()
        r1c1['state'] = tkinter.DISABLED
    else:
        row1col1.set(y)
        changeState()
        r1c1['state'] = tkinter.DISABLED
    if (row1col1.get() == x and row1col2.get() == x and row1col3.get() == x) or (row1col1.get() == x and row2col2.get() == x and row3col3.get() == x) or (row1col1.get() == x and row2col1.get() == x and row3col1.get() == x):
        winner = 'Player 1'
        Winner(winner)
        winner = ''
    if (row1col1.get() == y and row1col2.get() == y and row1col3.get() == y) or (row1col1.get() == y and row2col2.get() == y and row3col3.get() == y) or (row1col1.get() == y and row2col1.get() == y and row3col1.get() == y):
        winner = 'Player 2'
        Winner(winner)
        winner = ''

def btnTwoCmd(x, y, z):
    if playerOneBtn['state'] == tkinter.NORMAL:
        row1col2.set(x)
        changeState()
        r1c2['state'] = tkinter.DISABLED
    else:
        row1col2.set(y)
        changeState()
        r1c2['state'] = tkinter.DISABLED
    if (row1col1.get() == x and row1col2.get() == x and row1col3.get() == x) or (row1col2.get() == x and row2col2.get() == x and row3col2.get() == x):
        
        winner = 'Player 1'
        Winner(winner)
    if (row1col1.get() == y and row1col2.get() == y and row1col3.get() == y) or (row1col2.get() == y and row2col2.get() == y and row3col2.get() == y):
        
        winner = 'Player 2'
        Winner(winner)

def btnThreeCmd(x, y, z):
    if playerOneBtn['state'] == tkinter.NORMAL:
        row1col3.set(x)
        changeState()
        r1c3['state'] = tkinter.DISABLED
    else:
        row1col3.set(y)
        changeState()
        r1c3['state'] = tkinter.DISABLED
    if (row1col1.get() == x and row1col2.get() == x and row1col3.get() == x) or (row1col3.get() == x and row2col3.get() == x and row3col3.get() == x) or (row1col3.get() == x and row2col2.get() == x and row3col1.get() == x):
        
        winner = 'Player 1'
        Winner(winner)
    if (row1col1.get() == y and row1col2.get() == y and row1col3.get() == y) or (row1col3.get() == y and row2col3.get() == y and row3col3.get() == y) or (row1col3.get() == y and row2col2.get() == y and row3col1.get() == y):
        
        winner = 'Player 2'
        Winner(winner)

def btnFourCmd(x, y, z):
    if playerOneBtn['state'] == tkinter.NORMAL:
        row2col1.set(x)
        changeState()
        r2c1['state'] = tkinter.DISABLED
    else:
        row2col1.set(y)
        changeState()
        r2c1['state'] = tkinter.DISABLED
    if (row1col1.get() == x and row2col1.get() == x and row3col1.get() == x) or (row2col1.get() == x and row2col2.get() == x and row2col3.get() == x):
        
        winner = 'Player 1'
        Winner(winner)
    if (row1col1.get() == y and row2col1.get() == y and row3col1.get() == y) or (row2col1.get() == y and row2col2.get() == y and row2col3.get() == y):
        
        winner = 'Player 2'
        Winner(winner)

def btnFiveCmd(x, y, z):
    if playerOneBtn['state'] == tkinter.NORMAL:
        row2col2.set(x)
        changeState()
        r2c2['state'] = tkinter.DISABLED
    else:
        row2col2.set(y)
        changeState()
        r2c2['state'] = tkinter.DISABLED
    if (row1col2.get() == x and row2col2.get() == x and row3col3.get() == x) or (row1col2.get() == x and row2col2.get() == x and row3col2.get() == x) or (row1col3.get() == x and row2col2.get() == x and row3col1.get() == x)  or (row2col1.get() == x and row2col2.get() == x and row2col3.get() == x) or (row3col1.get() == x and row2col2.get() == x and row1col3.get() == x) or (row1col1.get() == x and row2col2.get() == x and row3col3.get() == x):
        
        winner = 'Player 1'
        Winner(winner)
    if (row1col2.get() == y and row2col2.get() == y and row3col3.get() == y) or (row1col2.get() == y and row2col2.get() == y and row3col2.get() == y) or (row1col3.get() == y and row2col2.get() == y and row3col1.get() == y)  or (row2col1.get() == y and row2col2.get() == y and row2col3.get() == y) or (row3col1.get() == y and row2col2.get() == y and row1col3.get() == y) or (row1col1.get() == y and row2col2.get() == y and row3col3.get() == y):
        
        winner = 'Player 2'
        Winner(winner)
    
def btnSixCmd(x, y, z):
    if playerOneBtn['state'] == tkinter.NORMAL:
        row2col3.set(x)
        changeState()
        r2c3['state'] = tkinter.DISABLED
    else:
        row2col3.set(y)
        changeState()
        r2c3['state'] = tkinter.DISABLED
    if (row1col3.get() == x and row2col3.get() == x and row3col3.get() == x) or (row2col1.get() == x and row2col2.get() == x and row2col3.get() == x):
        
        winner = 'Player 1'
        Winner(winner)
    if (row1col3.get() == y and row2col3.get() == y and row3col3.get() == y) or (row2col1.get() == y and row2col2.get() == y and row2col3.get() == y):
        
        winner = 'Player 2'
        Winner(winner)

def btnSevenCmd(x, y, z):
    if playerOneBtn['state'] == tkinter.NORMAL:
        row3col1.set(x)
        changeState()
        r3c1['state'] = tkinter.DISABLED
    else:
        row3col1.set(y)
        changeState()
        r3c1['state'] = tkinter.DISABLED
    if (row1col1.get() == x and row2col1.get() == x and row3col1.get() == x) or (row3col1.get() == x and row2col2.get() == x and row1col3.get() == x) or (row3col1.get() == x and row3col2.get() == x and row3col3.get() == x):
        winner = 'Player 1'
        Winner(winner)
        winner = ''
    if (row1col1.get() == y and row2col1.get() == y and row3col1.get() == y) or (row3col1.get() == y and row2col2.get() == y and row1col3.get() == y) or (row3col1.get() == y and row3col2.get() == y and row3col3.get() == y):
        winner = 'Player 2'
        Winner(winner)
        winner = ''

def btnEightCmd(x, y, z):
    if playerOneBtn['state'] == tkinter.NORMAL:
        row3col2.set(x)
        changeState()
        r3c2['state'] = tkinter.DISABLED
    else:
        row3col2.set(y)
        changeState()
        r3c2['state'] = tkinter.DISABLED
    if (row1col2.get() == x and row2col2.get() == x and row3col2.get() == x) or (row3col1.get() == x and row3col2.get() == x and row3col3.get() == x):
        
        winner = 'Player 1'
        Winner(winner)
    if (row1col2.get() == y and row2col2.get() == y and row3col2.get() == y) or (row3col1.get() == y and row3col2.get() == y and row3col3.get() == y):
        
        winner = 'Player 2'
        Winner(winner)

def btnNineCmd(x, y, z):
    if playerOneBtn['state'] == tkinter.NORMAL:
        row3col3.set(x)
        changeState()
        r3c3['state'] = tkinter.DISABLED
    else:
        row3col3.set(y)
        changeState()
        r3c3['state'] = tkinter.DISABLED
    if (row1col3.get() == x and row2col3.get() == x and row3col3.get() == x) or (row1col1.get() == x and row2col2.get() == x and row3col3.get() == x) or (row3col1.get() == x and row3col2.get() == x and row3col3.get() == x):
        
        winner = 'Player 1'
        Winner(winner)
    if (row1col3.get() == y and row2col3.get() == y and row3col3.get() == y) or (row1col1.get() == y and row2col2.get() == y and row3col3.get() == y) or (row3col1.get() == y and row3col2.get() == y and row3col3.get() == y):
        
        winner = 'Player 2'
        Winner(winner)



r1c1= tkinter.Button(root, textvariable=row1col1, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda b1 = 'Button 1': btnOneCmd("X", "O", b1), state= tkinter.NORMAL)
r1c1.place(x=70, y=100)

r1c2= tkinter.Button(root,textvariable=row1col2, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda b2 = 'Button 2': btnTwoCmd("X", "O", b2), state= tkinter.NORMAL)
r1c2.place(x=144, y=100)

r1c3 = tkinter.Button(root, textvariable=row1col3, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda b3 = 'Button 3': btnThreeCmd("X", "O", b3), state= tkinter.NORMAL)
r1c3.place(x=218, y=100)

r2c1 = tkinter.Button(root,textvariable=row2col1, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda b4 = 'Button 4': btnFourCmd("X", "O", b4), state= tkinter.NORMAL)
r2c1.place(x=70, y=175)

r2c2 = tkinter.Button(root, textvariable=row2col2, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda b5 = 'Button 5': btnFiveCmd("X", "O", b5), state= tkinter.NORMAL)
r2c2.place(x=144, y=175)

r2c3 = tkinter.Button(root, textvariable=row2col3, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda b6 = 'Button 6': btnSixCmd("X", "O", b6), state= tkinter.NORMAL)
r2c3.place(x=218, y=175)

r3c1= tkinter.Button(root,textvariable=row3col1, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda b7 = 'Button 7': btnSevenCmd("X", "O", b7), state= tkinter.NORMAL)
r3c1.place(x=70, y=250)

r3c2 = tkinter.Button(root, textvariable=row3col2, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda b8 = 'Button 8': btnEightCmd("X", "O", b8), state= tkinter.NORMAL)
r3c2.place(x=144, y=250)

r3c3 = tkinter.Button(root, textvariable=row3col3, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda b9 = 'Button 9': btnNineCmd("X", "O", b9), state= tkinter.NORMAL)
r3c3.place(x=218, y=250)


root.mainloop()
