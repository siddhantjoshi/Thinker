from tkinter import *

rootWidget = Tk()

def clickButton():
	labelWidget = Label(rootWidget, text = "Click On button !!")
	labelWidget.pack()

#no need to put parenthesis in tkinter
ButtonWidget = Button(rootWidget, text = "Click Me", command = clickButton)
ButtonWidget.pack()

rootWidget.mainloop()