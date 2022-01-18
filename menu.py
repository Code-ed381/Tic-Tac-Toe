import tkinter

parent_widget = tkinter.Tk()

def menu_callback():
    print("I'm in the menu callback!")
def submenu_callback():
    print("I'm in the submenu callback!")
    
menu_widget = tkinter.Menu(parent_widget)

submenu_widget = tkinter.Menu(menu_widget, tearoff=False)

submenu_widget.add_command(label="Submenu Item1", command=submenu_callback)

submenu_widget.add_command(label="Submenu Item2", command=submenu_callback)

menu_widget.add_cascade(label="Item1", menu=submenu_widget)

menu_widget.add_command(label="Item2", command=menu_callback)

menu_widget.add_command(label="Item3", command=menu_callback)

parent_widget.config(menu=menu_widget)

tkinter.mainloop()