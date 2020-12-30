# Andreas Westrell 2020
#
#

from tkinter import *
from tkinter import messagebox


version = 0.1

# -------------------------------------------
def About():
	messagebox.showinfo("About","@Text Editor Version: " + str(version) + " \n2020\nBy Andreas .")


# ------------------ Main program starts here -------------------------
#"WindowCreater"
root = Tk()
root.title("Text Editor ")
root.geometry("500x250")

# create a pulldown menu, and add it to the menu bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=Save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)

mainloop()
