# Andreas Westrell 2021


from tkinter import *
from tkinter import messagebox



version = 0.1

### Definitions
def About():
	messagebox.showinfo("About","PyPress " + str(version) +"\n2021 By Andreas Westrell")

# ------------------ Main program starts here -------------------------
root = Tk()
root.title("PyPress")
root.geometry("600x480")


mainloop()
