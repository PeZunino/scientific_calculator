import tkinter.ttk
from tkinter import *
import math

root = Tk()
root.title('Scientific Calculator')
root["bg"] = "black"

root.geometry('1300x556+200+200')
root.grid_rowconfigure(5, minsize=65)
root.overrideredirect(True)

#root.resizable(False, False)


f_number: float
second_number: float
math_type = ""
equal_lts_button = False
memory_sign_text = StringVar()
memory = 0


def handle_off():
    root.destroy()


def handle_equal():
    try:

        global second_number
        second_number = float(MainInput.get())

        MainInput.delete(0, END)

        global math_type

        if math_type == "":
            MainInput.insert(0, str(second_number))
        if math_type == "add":
            MainInput.insert(0, str(f_number + second_number))
        if math_type == "subtract":
            MainInput.insert(0, str(f_number - second_number))
        if math_type == "divide":
            MainInput.insert(0, str(f_number / second_number))
        if math_type == "multiply":
            MainInput.insert(0, str(f_number * second_number))
        if math_type == "raised":
            MainInput.insert(0, str(math.pow(f_number, second_number)))
        if math_type == "one_split":
            MainInput.insert(0, str(f_number * 1/second_number))
        if math_type == "square_num":
            MainInput.insert(0, str(math.pow(second_number, (1. / f_number))))
        if math_type == "log":
            MainInput.insert(0, str(math.log(f_number, second_number)))
        math_type = ""
        global equal_lts_button
        equal_lts_button = True
    except:
        print('error')


def handle_divide_button():
    try:

        first_number = MainInput.get()

        global f_number
        global math_type
        math_type = "divide"
        f_number = float(first_number)

        MainInput.delete(0, END)
        global equal_lts_button
        equal_lts_button = False
    except:
        print('error')

def handle_multiply_button():
    try:

        first_number = MainInput.get()

        global f_number
        global math_type
        math_type = "multiply"
        f_number = float(first_number)

        MainInput.delete(0, END)
        global equal_lts_button
        equal_lts_button = False
    except:
        print('error')

def handle_subtract_button():
    try:

        first_number = MainInput.get()

        global f_number
        global math_type
        math_type = "subtract"
        f_number = float(first_number)

        MainInput.delete(0, END)
        global equal_lts_button
        equal_lts_button = False
    except:
        print('error')

def handle_add_button():
    try:

        first_number = MainInput.get()

        global f_number
        global math_type
        math_type = "add"
        f_number = float(first_number)

        MainInput.delete(0, END)
        global equal_lts_button
        equal_lts_button = False

    except:
        print('error')
def handle_button_click(number):
    try:

        current_value = MainInput.get()

        MainInput.delete(0, END)

        global equal_lts_button

        if equal_lts_button:
            equal_lts_button = False
            MainInput.insert(0, str(number))

        else:
            MainInput.insert(0, str(current_value) + str(number))
    except:
        print('error')

def handle_clear_button():
    MainInput.delete(0, END)


def handle_memory_plus():
    try:

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
    except:
        print('error')

def handle_memory_minus():
    try:

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
    except:
        print('error')

def handle_memory_clean():
    try:

        global memory
        memory_sign_text.set('')
        memory = 0

    except:
        print('error')
def handle_memory_registry():
    try:

        MainInput.delete(0, END)
        MainInput.insert(0, str(memory))

        global equal_lts_button
        equal_lts_button = True
    except:
        print('error')

def validate_entry(s):
    operators = ['+', '-', '/', 'x', '.']

    if float(s) or s in operators:
        return True
    else:
        return False


def handle_raised_two():
    try:

        current_value = MainInput.get()

        MainInput.delete(0, END)

        MainInput.insert(0, math.pow(float(current_value), 2))

        global equal_lts_button
        equal_lts_button = True
    except:
        print('error')


def handle_raised_three():
    try:

        current_value = MainInput.get()

        MainInput.delete(0, END)

        MainInput.insert(0, math.pow(float(current_value), 2))

        global equal_lts_button
        equal_lts_button = True
    except:
        print('error')

def handle_raised_number_to_number():
    try:

        first_number = MainInput.get()

        global f_number
        global math_type
        math_type = "raised"
        f_number = float(first_number)

        MainInput.delete(0, END)
        global equal_lts_button
        equal_lts_button = False
    except:
        print('error')

def handle_ten_raised():
    try:

        current_value = MainInput.get()

        MainInput.delete(0, END)

        print(math.pow(float(current_value), 3))
        MainInput.insert(0, math.pow(10, float(current_value)))

        global equal_lts_button
        equal_lts_button = True
    except:
        print('error')


def handle_one_split_to():
    try:

        first_number = MainInput.get()

        global f_number
        global math_type
        math_type = "one_split"
        f_number = float(first_number)

        MainInput.delete(0, END)
        global equal_lts_button
        equal_lts_button = False
    except:
        print('error')

def handle_square(square_type: float):
    try:
        current_value = float(MainInput.get())

        MainInput.delete(0, END)

        MainInput.insert(0, str(math.pow(current_value, (1. / square_type))))

        global equal_lts_button
        equal_lts_button = True
    except:
        print('error')

def handle_square_number():
    try:
        first_number = MainInput.get()

        global f_number
        global math_type
        math_type = "square_num"
        f_number = float(first_number)


        MainInput.delete(0, END)
        global equal_lts_button
        equal_lts_button = False
    except:
        print('error')

def handle_angle(angle_type: str):
    try:
        current_value = float(MainInput.get())

        MainInput.delete(0, END)
        print(angle_type)
        match angle_type:
            case 'sin':
                MainInput.insert(0, str(math.sin(math.radians(current_value))))
            case 'cos':
                MainInput.insert(0, str(math.cos(math.radians(current_value))))
            case 'tan':
                MainInput.insert(0, str(math.tan(math.radians(current_value))))
            case 'sinh':
                MainInput.insert(0, str(math.sinh(current_value)))
            case 'cosh':
                MainInput.insert(0, str(math.cosh(current_value)))
            case 'tanh':
                MainInput.insert(0, str(math.tanh(current_value)))

        global equal_lts_button
        equal_lts_button = True
    except:
        print('error')

def handle_log():
    try:
        current_value = float(MainInput.get())

        MainInput.delete(0, END)

        MainInput.insert(0, math.log10(current_value))

        global equal_lts_button
        equal_lts_button = True

    except:
        print('error')

def handle_log_base():
    try:

        first_number = MainInput.get()

        global f_number
        global math_type
        math_type = "log"
        f_number = float(first_number)

        MainInput.delete(0, END)
        global equal_lts_button
        equal_lts_button = False

    except:
        print('error')
def handle_percent():
    try:
        global f_number


        global second_number

        result = f_number * second_number / 100

        MainInput.delete(0, END)

        MainInput.insert(0, str(result))

        global equal_lts_button
        equal_lts_button = True
    except:
        print('error')


def handle_AC():
    try:
        MainInput.delete(0, END)
        MainInput.insert(0, '0')
        global equal_lts_button
        equal_lts_button = True
    except:
        print('error')


def handle_sinal():
    try:
        current_value = float(MainInput.get())

        MainInput.delete(0, END)

        MainInput.insert(0, str(current_value * -1))
    except:
        print('error')
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
off_button = Button(root, numeric_button_style, text="Off", command= handle_off)

#Op buttons
add_button = Button(root, operator_button_style, text="+",  command=handle_add_button)
subtract_button = Button(root, operator_button_style, text="-",  command=handle_subtract_button)
divide_button = Button(root, operator_button_style, text="/",  command=handle_divide_button)
multiply_button = Button(root, operator_button_style, text="x",  command=handle_multiply_button)
equal_button = Button(root, operator_button_style, text="=", command=handle_equal)

#Main buttons
ac_button = Button(root, main_button_style, text="AC", command=handle_AC)
percent_button = Button(root, main_button_style, text="%", command=handle_percent)
change_operator_button = Button(root, main_button_style, text="+/-", command=handle_sinal)

#Sci buttons

#memory
memory_plus = Button(root, sci_button_style, text="M+", command=handle_memory_plus)
memory_minus = Button(root, sci_button_style, text="M-", command=handle_memory_minus)
memory_recall = Button(root, sci_button_style, text="MR", command=handle_memory_registry)
memory_clear = Button(root, sci_button_style, text="MC", command=handle_memory_clean)

#raised
number_raised_to_two = Button(root, sci_button_style, text="X??", command=handle_raised_two)
number_raised_to_three = Button(root, sci_button_style, text="X??", command=handle_raised_three)
number_raised_to_number = Button(root, sci_button_style, text="x^y", command=handle_raised_number_to_number)
one_split_button = Button(root, sci_button_style, text="1/x", command=handle_one_split_to)
ten_raised_to_number = Button(root, sci_button_style, text="10^x", command=handle_ten_raised)

#square
square_cubic = Button(root, sci_button_style, text="?????x", command=lambda: handle_square(3.0))
square = Button(root, sci_button_style, text="?????x", command=lambda: handle_square(2.0))
square_number = Button(root, sci_button_style, text="x???y", command=handle_square_number)

#angles
sin = Button(root, sci_button_style, text="sin", command=lambda: handle_angle('sin'))
cos = Button(root, sci_button_style, text="cos", command=lambda: handle_angle('cos'))
tan = Button(root, sci_button_style, text="tan", command=lambda: handle_angle('tan'))
sinh = Button(root, sci_button_style, text="sinh", command=lambda: handle_angle('sinh'))
cosh = Button(root, sci_button_style, text="cosh", command=lambda: handle_angle('cosh'))
tanh = Button(root, sci_button_style, text="tanh", command=lambda: handle_angle('tanh'))

#log
log = Button(root, sci_button_style, text="log10", command=handle_log)
log_base_diff = Button(root, sci_button_style, text="log(a,b)", command=handle_log_base)

MainInput.grid(row=0, column=0, columnspan=4, ipady=20, sticky="W")
memory_sign.grid(row=0, column=3)

memory_clear.grid(row=1, column=0)
memory_plus.grid(row=1, column=1)
memory_minus.grid(row=1, column=2)
memory_recall.grid(row=1, column=3)
ac_button.grid(row=1, column=4)
percent_button.grid(row=1, column=5)
change_operator_button.grid(row=1, column=6)
divide_button.grid(row=1, column=7)

number_raised_to_two.grid(row=2, column=0)
number_raised_to_three.grid(row=2, column=1)
number_raised_to_number.grid(row=2, column=2)
ten_raised_to_number.grid(row=2, column=3)
button_7.grid(row=2, column=4)
button_8.grid(row=2, column=5)
button_9.grid(row=2, column=6)
multiply_button.grid(row=2, column=7)

one_split_button.grid(row=3, column=0)
square.grid(row=3, column=1)
square_cubic.grid(row=3, column=2)
square_number.grid(row=3, column=3)
button_4.grid(row=3, column=4)
button_5.grid(row=3, column=5)
button_6.grid(row=3, column=6)
subtract_button.grid(row=3, column=7)

sin.grid(row=4, column=0)
cos.grid(row=4, column=1)
tan.grid(row=4, column=2)
log.grid(row=4, column=3)
button_1.grid(row=4, column=4)
button_2.grid(row=4, column=5)
button_3.grid(row=4, column=6)
add_button.grid(row=4, column=7)

sinh.grid(row=5, column=0)
cosh.grid(row=5, column=1)
tanh.grid(row=5, column=2)
log_base_diff.grid(row=5, column=3)
off_button.grid(row=5, column=4)
button_0.grid(row=5, column=5)
clear_button.grid(row=5, column=6)
equal_button.grid(row=5, column=7)

root.mainloop()
