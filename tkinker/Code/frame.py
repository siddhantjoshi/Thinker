from tkinter import *

rootWidget = Tk()
rootWidget.title("Frame")

frameWidget = LabelFrame(rootWidget, text="Frame 1 ", padx=50, pady=50)
frameWidget.grid(row = 0, column = 0)

frameWidget1 = LabelFrame(rootWidget, text="Frame 2 ", padx=50, pady=50)
frameWidget1.grid(row = 1, column = 0)

buttonWidget = Button(frameWidget, text= "Button")
buttonWidget.grid(row=0, column=0)

buttonWidget2 = Button(frameWidget1, text= "Button")
buttonWidget2.grid(row=0, column=0)

rootWidget.mainloop()