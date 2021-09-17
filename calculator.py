from tkinter import *

window =Tk()
window.title("My calculator")
window.minsize(width= 500, height= 400)

#functions
def add():
    first_value = int(textbox_1.get())
    second_value = int(textbox_2.get())
    answer =  first_value + second_value
    label_5["text"] = answer


def subtarct():
    first_value = int(textbox_1.get())
    second_value = int(textbox_2.get())
    answer = first_value - second_value
    label_5["text"] = answer


def multiply():
    first_value = int(textbox_1.get())
    second_value = int(textbox_2.get())
    answer = first_value * second_value
    label_5["text"] = answer


def divide():
    first_value = int(textbox_1.get())
    second_value = int(textbox_2.get())
    answer = first_value / second_value
    label_5["text"] = answer



#labels
label_1 = Label(text="Enter first number here")
label_1.grid(row=0, column= 0)

label_2 = Label(text="Enter your second number here")
label_2.grid(row=1, column=0)

label_3 = Label(text="What function would you like to pick")
label_3.grid(row=2, column=0)

label_4 = Label(text="Your answer is")


label_5 = Label()

#Textbox

textbox_1 = Entry()
textbox_1.grid(row= 0, column= 1)

textbox_2 = Entry()
textbox_2.grid(row=1, column=1)




#buttons

button_add = Button(text="ADD +", command= add)


button_sub = Button(text="SUBTRACT -", command= subtarct)

button_multiply = Button(text="MULTIPLY *", command= multiply)


button_divide = Button(text="DIVIDE /", command= divide)


window.mainloop()