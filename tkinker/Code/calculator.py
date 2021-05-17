from tkinter import *
rootWidget = Tk()
rootWidget.title("Calculator")

def getButton(number):
	curent = textBoxWidget.get()
	textBoxWidget.delete(0, END)
	textBoxWidget.insert(0, str(curent) + str(number))

def clearButton():
	textBoxWidget.delete(0,END)

def additionOperation():
	firstNumber = textBoxWidget.get()
	global fNum
	global op
	op = "additionOperation"
	fNum = int(firstNumber)
	textBoxWidget.delete(0, END)

def equalOperation():
	secondNumber = textBoxWidget.get()
	textBoxWidget.delete(0, END)

	if op == "additionOperation":
		textBoxWidget.insert(0, fNum + int(secondNumber))
	if op == "subOperation":
		textBoxWidget.insert(0, fNum - int(secondNumber))
	if op == "multipyOperation":
		textBoxWidget.insert(0, fNum * int(secondNumber))
	if op == "divideOperation":
		textBoxWidget.insert(0, fNum / int(secondNumber))

def subOperation():
	firstNumber = textBoxWidget.get()
	global fNum
	global op
	op = "subOperation"
	fNum = int(firstNumber)
	textBoxWidget.delete(0, END)

def multipyOperation():
	firstNumber = textBoxWidget.get()
	global fNum
	global op
	op = "multipyOperation"
	fNum = int(firstNumber)
	textBoxWidget.delete(0, END)

def divideOperation():
	firstNumber = textBoxWidget.get()
	global fNum
	global op
	op = "divideOperation"
	fNum = int(firstNumber)
	textBoxWidget.delete(0, END)

textBoxWidget = Entry(rootWidget, width= 35, borderwidth = 3)
textBoxWidget.grid(row= 0, column = 0,columnspan = 4, pady = 10 )

#initialize button
button_1 = Button(rootWidget, text = "1", padx= 40, pady = 20, command= lambda: getButton(1))
button_2 = Button(rootWidget, text = "2", padx= 40, pady = 20, command= lambda: getButton(2))
button_3 = Button(rootWidget, text = "3", padx= 40, pady = 20, command= lambda: getButton(3))
button_4 = Button(rootWidget, text = "4", padx= 40, pady = 20, command= lambda: getButton(4))
button_5 = Button(rootWidget, text = "5", padx= 40, pady = 20, command= lambda: getButton(5))
button_6 = Button(rootWidget, text = "6", padx= 40, pady = 20, command= lambda: getButton(6))
button_7 = Button(rootWidget, text = "7", padx= 40, pady = 20, command= lambda: getButton(7))
button_8 = Button(rootWidget, text = "8", padx= 40, pady = 20, command= lambda: getButton(8))
button_9 = Button(rootWidget, text = "9", padx= 40, pady = 20, command= lambda: getButton(9))
button_0 = Button(rootWidget, text = "0", padx= 40, pady = 20, command= lambda: getButton(0))

button_add = Button(rootWidget, text = "+", padx= 39, pady = 20, command= additionOperation)
button_multipy = Button(rootWidget, text = "*", padx= 39, pady = 20, command= multipyOperation)
button_sub = Button(rootWidget, text = "-", padx= 39, pady = 20, command= subOperation)
button_divide = Button(rootWidget, text = "/", padx= 39, pady = 20, command= divideOperation)

button_equalTo = Button(rootWidget, text = "=", padx= 91, pady = 20, command= equalOperation)
button_clear = Button(rootWidget, text = "Clear", padx= 79, pady = 20, command= clearButton)

#arrange button
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1 , columnspan = 2)

button_add.grid(row = 5, column = 0)
button_multipy.grid(row = 1, column = 3)
button_divide.grid(row = 2, column = 3)
button_sub.grid(row = 3, column = 3,)

button_equalTo.grid(row = 5, column = 1, columnspan = 2)


rootWidget.mainloop()