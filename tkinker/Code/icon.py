from tkinter import *
from PIL import Image, ImageTk

rootWidget = Tk()
rootWidget.title("Tkinter")
# # rootWidget.iconbitmap('Siddhnat Joshi.jpg')
imageWidget = ImageTk.PhotoImage(Image.open("Siddhnat Joshi.jpg"))
labelWidget = Label(image = imageWidget)
labelWidget.grid(row= 0, column= 0)
labelWidget2 = Label(rootWidget, text = "It's Me !!", bd=1, relief=SUNKEN)
labelWidget2.grid(row=1, column=0, sticky = W+E)
rootWidget.mainloop()

