from tkinter import *
from tkinter import messagebox

rootWidget = Tk()
rootWidget.title("Message Box Example")
def messageBox():
	response = messagebox.showinfo(title="Show Info", message="Message")
	Label(rootWidget, text = response).pack()

Button(rootWidget,text= "Click Me!!", command = messageBox).pack()

rootWidget.mainloop()