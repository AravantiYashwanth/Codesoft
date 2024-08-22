from tkinter import *



def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))


def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)


def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(END, f_num + int(second_number))
    elif math == "subtraction":
        entry.insert(END, f_num - int(second_number))
    elif math == "multiplication":
        entry.insert(END, f_num * int(second_number))
    elif math == "division":
        entry.insert(END, f_num / int(second_number))

window = Tk()
window.title("Calculator")
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)

entry = Entry(width=20)
entry.grid(column=1, row=0, columnspan=3)

button_1 = Button(text="1", command=lambda: button_click(1))
button_1.grid(column=1, row=1)

button_2 = Button(text="2", command=lambda: button_click(2))
button_2.grid(column=2, row=1)

button_3 = Button(text="3", command=lambda: button_click(3))
button_3.grid(column=3, row=1)

button_4 = Button(text="4", command=lambda: button_click(4))
button_4.grid(column=1, row=2)

button_5 = Button(text="5", command=lambda: button_click(5))
button_5.grid(column=2, row=2)

button_6 = Button(text="6", command=lambda: button_click(6))
button_6.grid(column=3, row=2)

button_7 = Button(text="7", command=lambda: button_click(7))
button_7.grid(column=1, row=3)

button_8 = Button(text="8", command=lambda: button_click(8))
button_8.grid(column=2, row=3)

button_9 = Button(text="9", command=lambda: button_click(9))
button_9.grid(column=3, row=3)

button_0 = Button(text="0", command=lambda: button_click(0))
button_0.grid(column=2, row=4)

button_add = Button(text="+", command=button_add)
button_add.grid(column=1, row=5)


button_subtract = Button(text="-", command=button_subtract)
button_subtract.grid(column=2, row=5)

button_multiply = Button(text="x", command=button_multiply)
button_multiply.grid(column=3, row=5)

button_divide = Button(text="/", command=button_divide)
button_divide.grid(column=1, row=6)

button_equal = Button(text="=", command=button_equal)
button_equal.grid(column=2, row=6)

button_clear = Button(text="Clear", command=button_clear)
button_clear.grid(column=3, row=6)

window.mainloop()
