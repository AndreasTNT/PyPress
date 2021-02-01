# Andreas Westrell 2020
#
#

from tkinter import *
from tkinter import messagebox


version = 0.1

# -------------------------------------------
def About():
	messagebox.showinfo("About","Word processor " + str(version) +"\n2020 By Andreas Westrell")


# ------------------ Main program starts here -------------------------
#"WindowCreater"
root = Tk()
root.title("Word processor")
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
menubar.add_cascade(label= "View", menu=viewmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

### Menus
# File menu
filemenu.add_command(label="New")
filemenu.add_command(label="New Window")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as")
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
formatmenu.add_checkbutton(Text="Word Wrap", Variable=Wordwrap, onvalue=1, offvalue=0, command=Check_wordwrap)
formatmenu.add_command(label="")
# View menu
# Help menu
helpmenu.add_command(label="About", command=About)


# display the menu
root.config(menu=menubar)

mainloop()
