from tkinter import *


root = Tk()
root.title('Scientific Calculator')

root["bg"] = "black"

width = 500
height = 200
root.resizable(False, False)
root.geometry("%dx%d" % (width, height))


f_number = 0
math_type = ""
equal_lts_button = False
Font_tuple = ("Helvetica", 20, "bold")


def handle_equal():
    second_number = MainInput.get()
    MainInput.delete(0, END)

    if math_type == "add":
        MainInput.insert(0, f_number + int(second_number))
    if math_type == "subtract":
        MainInput.insert(0, f_number - int(second_number))
    if math_type == "divide":
        MainInput.insert(0, f_number / int(second_number))
    if math_type == "multiply":
        MainInput.insert(0, f_number * int(second_number))

    global equal_lts_button
    equal_lts_button = True


def handle_divide_button():
    first_number = MainInput.get()

    global f_number
    global math_type
    math_type = "divide"
    f_number = int(first_number)

    MainInput.delete(0, END)
    global equal_lts_button
    equal_lts_button = False


def handle_multiply_button():
    first_number = MainInput.get()

    global f_number
    global math_type
    math_type = "multiply"
    f_number = int(first_number)

    MainInput.delete(0, END)
    global equal_lts_button
    equal_lts_button = False


def handle_subtract_button():
    first_number = MainInput.get()

    global f_number
    global math_type
    math_type = "subtract"
    f_number = int(first_number)

    MainInput.delete(0, END)
    global equal_lts_button
    equal_lts_button = False


def handle_add_button():
    first_number = MainInput.get()

    global f_number
    global math_type
    math_type = "add"
    f_number = int(first_number)

    MainInput.delete(0, END)
    global equal_lts_button
    equal_lts_button = False


def handle_button_click(number):
    current_value = MainInput.get()

    MainInput.delete(0, END)

    if(equal_lts_button):
        MainInput.insert(0, str(number))

    else:
        MainInput.insert(0, str(current_value) + str(number))


def handle_clear_button():
    MainInput.delete(0, END)


def validate_entry(s):
    if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False


button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: handle_button_click(0), font=Font_tuple)
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: handle_button_click(1), font=Font_tuple)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: handle_button_click(2), font=Font_tuple)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: handle_button_click(3), font=Font_tuple)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: handle_button_click(4), font=Font_tuple)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: handle_button_click(5), font=Font_tuple)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: handle_button_click(6), font=Font_tuple)
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: handle_button_click(7), font=Font_tuple)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: handle_button_click(8), font=Font_tuple)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: handle_button_click(9), font=Font_tuple)

add_button = Button(root, text="   +   ", padx=55, pady=20, command=handle_add_button, font=Font_tuple)
subtract_button = Button(root, text="    -   ", padx=55, pady=20, command=handle_subtract_button, font=Font_tuple)
divide_button = Button(root, text="   /   ", padx=55, pady=20, command=handle_divide_button, font=Font_tuple)
multiply_button = Button(root, text="    *   ", padx=55, pady=20, command=handle_multiply_button, font=Font_tuple)
equal_button = Button(root, text="   =   ", padx=55, pady=20, command=handle_equal, font=Font_tuple)
clear_button = Button(root, text="Clear", padx=35, pady=15, command=handle_clear_button, font=Font_tuple)

vcm = (root.register(validate_entry), "%S")
MainInput = Entry(root, width=35, borderwidth=0, highlightthickness=0, font=Font_tuple, bg="black", fg="white",
                  validate='key', vcmd=vcm)

MainInput.insert(0, '0')
MainInput.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#clear_button.grid(row=0, column=3)

#button_7.grid(row=1, column=0)
#button_8.grid(row=1, column=1)
#button_9.grid(row=1, column=2)
#multiply_button.grid(row=1, column=3)

#button_4.grid(row=2, column=0)
#button_5.grid(row=2, column=1)
#button_6.grid(row=2, column=2)
#subtract_button.grid(row=2, column=3)

#button_1.grid(row=3, column=0)
#button_2.grid(row=3, column=1)
#button_3.grid(row=3, column=2)
#add_button.grid(row=3, column=3)

#button_0.grid(row=4, column=1)
#equal_button.grid(row=4, column=3)

root.mainloop()
