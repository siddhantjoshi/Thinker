from tkinter import *

#define roor widget's
rootWidget = Tk()

#define widget's
labelWidget = Label(rootWidget, text = "Hello User !!!")
labelTowWidget = Label(rootWidget, text = "Siddhnat")

#positioin of widget's
labelWidget.grid(row = 0, column =2 )
labelTowWidget.grid(row = 1, column = 1 )

#fit the widget's in loop 
rootWidget.mainloop()