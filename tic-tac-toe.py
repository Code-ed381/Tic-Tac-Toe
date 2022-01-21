import tkinter
from tkinter import *
from tkinter import Menu
from tkinter.constants import DISABLED, NORMAL

root = tkinter.Tk()

root.resizable(0, 0)

root.geometry('355x400')

root.title('Tic-Tac-Toe')

root.configure(bg='#36454F')



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

#Menu commands and widgets for newgame, exit and help
def MenuCmd():
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

    playerOneBtn['state'] = tkinter.NORMAL
    playerOneBtn['bg'] = 'green'
    playerOneBtn['fg'] = 'white'

    playerTwoBtn['state'] = tkinter.DISABLED
    playerTwoBtn['bg'] = 'red'
    playerTwoBtn['fg'] = 'black'

menu_widget = Menu(root)
root.config(menu=menu_widget)

submenu_widget = Menu(menu_widget, tearoff=FALSE)
submenu_widget.add_command(label='New game', command=MenuCmd)
submenu_widget.add_command(label='Exit', command=lambda: root.destroy())

menu_widget.add_cascade(label="Options", menu=submenu_widget)
menu_widget.add_command(label="Help", command=Help)


#Changes the state of player buttons from Normal to Disabled and vice versa when game buttons are clicked
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

#Player buttons, shows the next and current player
playerOneBtn = tkinter.Button(root, text='Player 1 (X)', fg='white', bg='green', font="Arial 10", state=NORMAL)
playerOneBtn.place(x=80, y=40)

playerTwoBtn = tkinter.Button(root, text='Player 2 (O)', fg='black', bg='red',font="Arial 10", state=DISABLED)
playerTwoBtn.place(x=185, y=40)


#String variables of game buttons, grabs the values of the buttons for further manipulation
row1col1 = StringVar()
row1col2 = StringVar()
row1col3 = StringVar()
row2col1 = StringVar()
row2col2 = StringVar()
row2col3 = StringVar()
row3col1 = StringVar()
row3col2 = StringVar()
row3col3 = StringVar()


#Restarts the game when new game is pressed
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
    
    
#Opens another tkinter window to display the results of the game
def Winner(winner):
    if winner == 'Player 1':
        winMessage = Toplevel(master=None)
        winMessage.title("Winner")
        winMessage.geometry('300x200')
        winMessage.config(bg='white')

        winnerText = tkinter.Label(winMessage,text='Player one won the game', bg='white',fg='green', font='Calibri 12')
        winnerText.place(x=42, y=30)
        newgame = tkinter.Button(winMessage, text='New game', font='Arial 12', command= lambda : Restart(winMessage))
        newgame.place(x=100, y=65)
        newgame = tkinter.Button(winMessage, text='Exit', font='Arial 12', command = lambda: root.destroy())
        newgame.place(x=127, y=105)

    elif winner == 'Player 2':
        winMessage = Toplevel(master=None)
        winMessage.title("Winner")
        winMessage.geometry('300x200')
        winMessage.config(bg='white')

        winnerText = tkinter.Label(winMessage,text='Player two won the game', bg='white', fg='red', font='Calibri 12')
        winnerText.place(x=42, y=30)
        newgame = tkinter.Button(winMessage, text='New game', font='Arial 12', command= lambda : Restart(winMessage))
        newgame.place(x=100, y=65)
        newgame = tkinter.Button(winMessage, text='Exit', font='Arial 12', command = lambda: root.destroy())
        newgame.place(x=127, y=105)
    elif winner != 'Player 1' or winner != 'Player 2':
            if row1col1.get() != '':
                if row1col2.get() != '':
                    if row1col3.get() != '':
                        if row2col1.get() != '':
                            if row2col2.get() != '':
                                if row2col3.get() != '':
                                    if row3col1.get() != '':
                                        if row3col2.get() != '':
                                            if row3col3.get() != '':
                                                winMessage = Toplevel(master=None)
                                                winMessage.title("Winner")
                                                winMessage.geometry('300x200')
                                                winMessage.config(bg='white')

                                                winnerText = tkinter.Label(winMessage,text="It's a draw game", bg='white', fg='blue', font='Calibri 12')
                                                winnerText.place(x=80, y=30)
                                                newgame = tkinter.Button(winMessage, text='New game', font='Arial 12', command= lambda : Restart(winMessage))
                                                newgame.place(x=100, y=65)
                                                newgame = tkinter.Button(winMessage, text='Exit', font='Arial 12', command = lambda: root.destroy())
                                                newgame.place(x=127, y=105)

#Game buttons functions from button to button nine
def btnOneCmd(x, y):
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
    if (row1col1.get() == y and row1col2.get() == y and row1col3.get() == y) or (row1col1.get() == y and row2col2.get() == y and row3col3.get() == y) or (row1col1.get() == y and row2col1.get() == y and row3col1.get() == y):
        winner = 'Player 2'
        Winner(winner)
    else:
        winner = ''
        Winner(winner)

def btnTwoCmd(x, y):
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
    else:
        winner = ''
        Winner(winner)

def btnThreeCmd(x, y):
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
    else:
        winner = ''
        Winner(winner)

def btnFourCmd(x, y):
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
    else:
        winner = ''
        Winner(winner)

def btnFiveCmd(x, y):
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
    else:
        winner = ''
        Winner(winner)
    
def btnSixCmd(x, y):
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
    else:
        winner = ''
        Winner(winner)

def btnSevenCmd(x, y):
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
    if (row1col1.get() == y and row2col1.get() == y and row3col1.get() == y) or (row3col1.get() == y and row2col2.get() == y and row1col3.get() == y) or (row3col1.get() == y and row3col2.get() == y and row3col3.get() == y):
        winner = 'Player 2'
        Winner(winner)
    else:
        winner = ''
        Winner(winner)

def btnEightCmd(x, y):
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
    else:
        winner = ''
        Winner(winner)

def btnNineCmd(x, y):
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
    else:
        winner = ''
        Winner(winner)


#Game buttons
r1c1= tkinter.Button(root, textvariable=row1col1, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda: btnOneCmd("X", "O"), state= tkinter.NORMAL)
r1c1.place(x=70, y=100)

r1c2= tkinter.Button(root,textvariable=row1col2, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda: btnTwoCmd("X", "O"), state= tkinter.NORMAL)
r1c2.place(x=144, y=100)

r1c3 = tkinter.Button(root, textvariable=row1col3, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda: btnThreeCmd("X", "O",), state= tkinter.NORMAL)
r1c3.place(x=218, y=100)

r2c1 = tkinter.Button(root,textvariable=row2col1, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda: btnFourCmd("X", "O",), state= tkinter.NORMAL)
r2c1.place(x=70, y=175)

r2c2 = tkinter.Button(root, textvariable=row2col2, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda: btnFiveCmd("X", "O",), state= tkinter.NORMAL)
r2c2.place(x=144, y=175)

r2c3 = tkinter.Button(root, textvariable=row2col3, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda: btnSixCmd("X", "O",), state= tkinter.NORMAL)
r2c3.place(x=218, y=175)

r3c1= tkinter.Button(root,textvariable=row3col1, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda: btnSevenCmd("X", "O",), state= tkinter.NORMAL)
r3c1.place(x=70, y=250)

r3c2 = tkinter.Button(root, textvariable=row3col2, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda: btnEightCmd("X", "O",), state= tkinter.NORMAL)
r3c2.place(x=144, y=250)

r3c3 = tkinter.Button(root, textvariable=row3col3, font="Arial 20",bg='#F4BB44', width='3', height='2', command=lambda: btnNineCmd("X", "O",), state= tkinter.NORMAL)
r3c3.place(x=218, y=250)


root.mainloop()
