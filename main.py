from tkinter import *

window =Tk()
window.title("Miles to km converter")
window.minsize(width= 500, height= 400)


def button_clicked():
    user_input = int(textbox.get())
    answer = user_input * 1.609344
    label_3["text"] = answer

#labels
label_1 = Label(text="Miles", font=("Arial", 20, "italic"))
label_1.grid(column=3, row=1)

label_2 = Label(text= "is equal to" , font=("Arial", 20, "italic"))
label_2.grid(column=1, row=2)

label_3 = Label(text= 0, font=("Arial", 12,))
label_3.grid(column=2, row=2)

label_4 = Label(text= "KM", font=("Arial", 20, "italic"))
label_4.grid(column=3, row=2)

#textbox
textbox = Entry()
textbox.grid(column=2, row=1)

#button
button = Button(text= "Convert", command= button_clicked)
button.grid(column=2, row=3)









window.mainloop()