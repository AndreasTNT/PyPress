# Andreas Westrell 2021


from tkinter import *
from tkinter import messagebox



version = 0.1

### Definitions
def About():
	messagebox.showinfo("About","PyPress " + str(version) +"\n2021 By Andreas Westrell")

# Wordwrap
# Figure out how to do 'Wordwrap = Tk.IntVar()'
# def Check_wordwrap():
# 	Wordwrap.get() 

# ------------------ Main program starts here -------------------------
root = Tk()
root.title("PyPress")
root.geometry("500x250")

### Menu bar and define extra menus
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)
formatmenu = Menu(menubar, tearoff=0)
viewmenu = Menu(menubar , tearoff=0)
helpmenu = Menu(menubar, tearoff=0)
# init the menus
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label= "Edit", menu=editmenu)
menubar.add_cascade(label= "Format", menu=formatmenu)
# menubar.add_cascade(label= "View", menu=viewmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

### Menus
# File menu
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
# Edit menu
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_separator()
editmenu.add_command(label="Find")
editmenu.add_command(label="Replace")
editmenu.add_command(label="Go To")
editmenu.add_separator()
editmenu.add_command(label="Select All")
editmenu.add_command(label="Time/Date")
# Format menu
# Figure out how to do format menu and wordwrap checkbutton
# formatmenu.add_checkbutton(Text="Word Wrap", Variable=Wordwrap, onvalue=1, offvalue=0, command=Check_wordwrap)

# TODO FONT formatmenu.add_command(label="Font", command=Font)

# View menu
# Help menu
helpmenu.add_command(label="About PyPress", command=About)


# display the menu
root.config(menu=menubar)

mainloop()
