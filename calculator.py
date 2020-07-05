from tkinter import *
import math

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)


def myClick():
    hello = "Hello" + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


def button_click(numbers):
    current_num = e.get()
    e.delete(0, END)
    e.insert(0, str(current_num) + str(numbers))


def button_add():
    first_num = e.get()
    global f_num
    global math_v
    math_v = "addition"
    f_num = float(first_num)
    e.delete(0, END)


def button_clear():
    e.delete(0, END)


def button_sub():
    first_num = e.get()
    global f_num
    global math_v
    math_v = "subtraction"
    f_num = float(first_num)
    e.delete(0, END)


def button_multi():
    first_num = e.get()
    global f_num
    global math_v
    math_v = "multiplication"
    f_num = float(first_num)
    e.delete(0, END)


def button_divide():
    first_num = e.get()
    global f_num
    global math_v
    math_v = "division"
    f_num = float(first_num)
    e.delete(0, END)


def button_sqrt():
    num = e.get()
    global f_num
    global math_v
    math_v = "sqrt"
    f_num = float(math.sqrt(int(num)))
    e.delete(0, END)

def button_equal():
    second_num = e.get()
    e.delete(0, END)

    if math_v == "addition":
        e.insert(0, f_num + int(second_num))
    if math_v == "subtraction":
        e.insert(0, f_num - int(second_num))
    if math_v == "multiplication":
        e.insert(0, f_num * int(second_num))
    if math_v == "division":
        e.insert(0, f_num / int(second_num))
    if math_v == "sqrt":
        e.insert(0, f_num)



# create button

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=40.5, pady=20, command=button_sub)
button_multi = Button(root, text="*", padx=40.5, pady=20, command=button_multi)
button_divide = Button(root, text="/", padx=40.49, pady=20, command=button_divide)
button_equal = Button(root, text="=", padx=39, pady=20, command=button_equal)
button_clear = Button(root, text="CC", padx=34.5, pady=20, command=button_clear)
button_sqrt = Button(root, text="sqrt", padx=33, pady=20, command=button_sqrt)

button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)
button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)
button_0.grid(row=4, column=1)
button_add.grid(row=4, column=2)
button_clear.grid(row=4, column=3)
button_sub.grid(row=5, column=1)
button_multi.grid(row=5, column=2)
button_divide.grid(row=5, column=3)
button_equal.grid(row=6, column=1)
button_sqrt.grid(row=6, column=2)

root.mainloop()
