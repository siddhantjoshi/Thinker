from tkinter import *

rootWidget = Tk()
#input label widget's
entryWidget = Entry(rootWidget, width = 50)
entryWidget.pack()
#get default placehoder
entryWidget.insert(0,"Enter text")

def clickButton():
	labelWidget = Label(rootWidget, text = entryWidget.get())
	labelWidget.pack()

#no need to put parenthesis in tkinter
#button Widget
ButtonWidget = Button(rootWidget, text = "Click Me", command = clickButton).pack()

rootWidget.mainloop()