#Import necessary Library
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
#Create an instance of tkinter window
win= Tk()
#Set the geometry of tkinter window
win.geometry("750x250")
#Define the function to change the value in label widget
def change_text(label):
    label.configure(text= "Hey, I am Label-2", background="gray91")
#Create a Label
label = Label(win, text= "Hey, I am Label-1", font= ('Helvetica 15 underline'), background="gray76")
label.pack(pady=20)
#Create a button
btn= ttk.Button(win,text= "Change", command=lambda:change_text(label), state= DISABLED)
btn.pack(pady=10)
win.mainloop()