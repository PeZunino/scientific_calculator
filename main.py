import tkinter.ttk
from tkinter import *


root = Tk()
root.title('Scientific Calculator')
root["bg"] = "black"

root.grid_rowconfigure(5, minsize=65)

#root.resizable(False, False)


f_number: float
math_type = ""
equal_lts_button = False
memory_sign_text = StringVar()
memory = 0


def handle_equal():
    second_number = MainInput.get()
    MainInput.delete(0, END)

    global math_type

    if math_type == "":
        MainInput.insert(0, str(second_number))
    if math_type == "add":
        MainInput.insert(0, str(f_number + float(second_number)))
    if math_type == "subtract":
        MainInput.insert(0, str(f_number - float(second_number)))
    if math_type == "divide":
        MainInput.insert(0, str(f_number / float(second_number)))
    if math_type == "multiply":
        MainInput.insert(0, str(f_number * float(second_number)))

    math_type = ""
    global equal_lts_button
    equal_lts_button = True


def handle_divide_button():
    first_number = MainInput.get()

    global f_number
    global math_type
    math_type = "divide"
    f_number = float(first_number)

    MainInput.delete(0, END)
    global equal_lts_button
    equal_lts_button = False


def handle_multiply_button():
    first_number = MainInput.get()

    global f_number
    global math_type
    math_type = "multiply"
    f_number = float(first_number)

    MainInput.delete(0, END)
    global equal_lts_button
    equal_lts_button = False


def handle_subtract_button():
    first_number = MainInput.get()

    global f_number
    global math_type
    math_type = "subtract"
    f_number = float(first_number)

    MainInput.delete(0, END)
    global equal_lts_button
    equal_lts_button = False


def handle_add_button():
    first_number = MainInput.get()

    global f_number
    global math_type
    math_type = "add"
    f_number = float(first_number)

    MainInput.delete(0, END)
    global equal_lts_button
    equal_lts_button = False


def handle_button_click(number):
    current_value = MainInput.get()

    MainInput.delete(0, END)

    global equal_lts_button

    if equal_lts_button:
        equal_lts_button = False
        MainInput.insert(0, str(number))

    else:
        MainInput.insert(0, str(current_value) + str(number))


def handle_clear_button():
    MainInput.delete(0, END)


def handle_memory_plus():
    current_value = MainInput.get()

    memory_sign_text.set('M')

    global memory

    print(float(current_value))
    print(memory)

    memory = memory + float(current_value)

    MainInput.delete(0, END)
    MainInput.insert(0, str(memory))

    global equal_lts_button
    equal_lts_button = True


def handle_memory_minus():
    current_value = MainInput.get()

    memory_sign_text.set('M')

    global memory

    print(float(current_value))
    print(memory)

    memory = memory - float(current_value)

    MainInput.delete(0, END)
    MainInput.insert(0, str(memory))

    global equal_lts_button
    equal_lts_button = True


def handle_memory_clean():
    global memory
    memory_sign_text.set('')
    memory = 0


def handle_memory_registry():
    MainInput.delete(0, END)
    MainInput.insert(0, str(memory))

    global equal_lts_button
    equal_lts_button = True


def validate_entry(s):
    operators = ['+', '-', '/', 'x', '.']

    if float(s) or s in operators:
        return True
    else:
        return False


vcm = (root.register(validate_entry), "%S")


buttons_width = 10

numeric_button_style = {
    "background": "#505050",
    "fg": "white",
    "font": "Myriad 20 bold",
    "borderwidth": 0,
    "highlightthickness": 0,
    "width": buttons_width,
    "height": 3,

}

operator_button_style = {
    "background": "#FF9500",
    "font": "Myriad 20 bold",
    "borderwidth": 0,
    "highlightthickness": 0,
    "width": buttons_width,
    "height": 3,
}

main_button_style = {
    "background": "#D4D4D2",
    "font": "Myriad 20 bold",
    "borderwidth": 0,
    "highlightthickness": 0,
    "width": buttons_width,
    "height": 3,
}

sci_button_style = {
    "background": "#262626",
    "font": "Myriad 20 bold",
    "borderwidth": 0,
    "highlightthickness": 0,
    "width": buttons_width,
    "height": 3,
}

entry_style = {
    "width": 35,
    "borderwidth": 0,
    "highlightthickness": 0,
    "font": 'Myriad 20 bold',
    "bg": "black",
    "fg": "white",
}

memory_label_style = {
    "bg": "black",
    "fg": "white",
    "font": "Myriad 20 bold",
    "borderwidth": 0,
    "highlightthickness": 0,
    "width": buttons_width,
    "height": 3,
}


MainInput = Entry(root, entry_style, validate='all', vcmd=vcm)
memory_sign = Label(root, memory_label_style, textvariable=memory_sign_text)

#Num buttons
button_0 = Button(root, numeric_button_style, text="0", command=lambda: handle_button_click(0))
button_1 = Button(root, numeric_button_style, text="1",  command=lambda: handle_button_click(1))
button_2 = Button(root, numeric_button_style, text="2",  command=lambda: handle_button_click(2))
button_3 = Button(root, numeric_button_style, text="3", command=lambda: handle_button_click(3))
button_4 = Button(root, numeric_button_style, text="4", command=lambda: handle_button_click(4))
button_5 = Button(root, numeric_button_style, text="5", command=lambda: handle_button_click(5))
button_6 = Button(root, numeric_button_style, text="6",  command=lambda: handle_button_click(6))
button_7 = Button(root, numeric_button_style, text="7", command=lambda: handle_button_click(7))
button_8 = Button(root, numeric_button_style, text="8",  command=lambda: handle_button_click(8))
button_9 = Button(root, numeric_button_style, text="9", command=lambda: handle_button_click(9))

#Special Buttons
clear_button = Button(root, numeric_button_style, text="Clear", command=handle_clear_button)
eq_segundo_gr = Button(root, numeric_button_style, text="Eq 2", command=lambda: handle_button_click(0))

#Op buttons
add_button = Button(root, operator_button_style, text="+",  command=handle_add_button)
subtract_button = Button(root, operator_button_style, text="-",  command=handle_subtract_button)
divide_button = Button(root, operator_button_style, text="/",  command=handle_divide_button)
multiply_button = Button(root, operator_button_style, text="x",  command=handle_multiply_button)
equal_button = Button(root, operator_button_style, text="=", command=handle_equal)

#Main buttons
on_off_button = Button(root, main_button_style, text="AC")
percent_button = Button(root, main_button_style, text="%")
change_operator_button = Button(root, main_button_style, text="+/-")

#Sci buttons
memory_plus = Button(root, sci_button_style, text="M+", command=handle_memory_plus)
memory_minus = Button(root, sci_button_style, text="M-", command=handle_memory_minus)
memory_recall = Button(root, sci_button_style, text="MR", command=handle_memory_registry)
memory_clear = Button(root, sci_button_style, text="MC", command=handle_memory_clean)


MainInput.grid(row=0, column=0, columnspan=4, ipady=20,sticky="W")
memory_sign.grid(row=0, column=3)

memory_plus.grid(row=1, column=0)
memory_minus.grid(row=1, column=1)
memory_recall.grid(row=1, column=2)
memory_clear.grid(row=1, column=3)
on_off_button.grid(row=1, column=4)
percent_button.grid(row=1, column=5)
change_operator_button.grid(row=1, column=6)
divide_button.grid(row=1, column=7)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
multiply_button.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
subtract_button.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
add_button.grid(row=4, column=3)

button_0.grid(row=5, column=0)
eq_segundo_gr.grid(row=5, column=1)
clear_button.grid(row=5, column=2)
equal_button.grid(row=5, column=3)

root.mainloop()
