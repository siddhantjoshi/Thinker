from tkinter import *

rootWidget = Tk()
rootWidget.title("New Window")
def openWindow():
	newWidget = Tk()
	newWidget.title("New Window")
	rootWidget.destroy()

buttonWidget = Button(rootWidget, text="Click Me!!", command= openWindow).pack()
rootWidget.mainloop()