from tkinter import *
import math

window = Tk()
window.title('Calculator')
window.geometry('260x270')

entry = StringVar()
num1 = ''
operator = ''
operators = ['+', '-', '*', '/']


def btn_press(button):
    """This function will allow for a button press to add the corresponding number or operator to the equation"""
    global entry, num1, operator, operators

    # Pressing an operator will store the first number and the operator pressed for later use
    if button in operators:
        num1 = entry.get()
        operator = button
        entry.set('')
    elif button == '+-':
        # the negative button will check if a number is already a negative and reverse it
        if '-' in entry.get():
            temp_entry = entry.get()
            change = temp_entry[1:]
            entry.set(change)
        # otherwise make number a negative
        else:
            entry.set('-' + entry.get())
    elif button == '.':
        # the decimal button will evaluate weather or not a decimal already exists in the entry and pass if true
        if '.' in entry.get():
            pass
        # otherwise add a decimal
        else:
            entry.set(entry.get() + button)
    else:
        entry.set(entry.get() + button)


def clear_press(button):
    """This will run the functionality for both the clear button and the backspace button"""
    global entry

    # clear button will reset the entry box
    if button == 'C':
        entry.set('')
    # backspace button will clear the last index in a sting
    elif button == 'B':
        temp_entry = entry.get()
        back_entry = temp_entry[:-1]
        entry.set(back_entry)


def equal_press(button):
    """This will run the functionality for the equals and square root button"""
    global entry, num1, operator

    if button == '=':
        # Try block will handle exceptions for errors
        try:
            answer = eval(num1 + operator + entry.get())
            entry.set(answer)
        except ZeroDivisionError:
            entry.set('Cannot divide by zero.     ')
        except SyntaxError:
            entry.set('Invalid equation.               ')
    elif button == 'SQRT':
        # Try block will handle exceptions for errors
        try:
            sq = math.sqrt(int(entry.get()))
            entry.set(sq)
        except ValueError:
            entry.set('Invalid Entry                   ')


# this code adds all buttons and creates the aesthetics of the calculator as well as adding commands
clear_btn = Button(window, text='C', width=7, height=2, bg='Red', command=lambda: clear_press('C'))
clear_btn.grid(row=2, column=0, padx=3, pady=3)

backspace_btn = Button(window, text='->', width=7, height=2, bg='Light Grey', command=lambda: clear_press('B'))
backspace_btn.grid(row=2, column=1, padx=3, pady=3)

negative_btn = Button(window, text='-/+', width=7, height=2, bg='Light Grey', command=lambda: btn_press('+-'))
negative_btn.grid(row=2, column=2, padx=3, pady=3)

sqrt_btn = Button(window, text='√', width=7, height=2, bg='Light Grey', command=lambda: equal_press('SQRT'))
sqrt_btn.grid(row=2, column=3, padx=3, pady=3)

seven_btn = Button(window, text='7', width=7, height=2, bg='Grey', command=lambda: btn_press('7'))
seven_btn.grid(row=3, column=0, padx=3, pady=3)

eight_btn = Button(window, text='8', width=7, height=2, bg='Grey', command=lambda: btn_press('8'))
eight_btn.grid(row=3, column=1, padx=3, pady=3)

nine_btn = Button(window, text='9', width=7, height=2, bg='Grey', command=lambda: btn_press('9'))
nine_btn.grid(row=3, column=2, padx=3, pady=3)

divide_btn = Button(window, text='÷', width=7, height=2, bg='Light Grey', command=lambda: btn_press('/'))
divide_btn.grid(row=3, column=3, padx=3, pady=3)

four_btn = Button(window, text='4', width=7, height=2, bg='Grey', command=lambda: btn_press('4'))
four_btn.grid(row=4, column=0, padx=3, pady=3)

five_btn = Button(window, text='5', width=7, height=2, bg='Grey', command=lambda: btn_press('5'))
five_btn.grid(row=4, column=1, padx=3, pady=3)

six_btn = Button(window, text='6', width=7, height=2, bg='Grey', command=lambda: btn_press('6'))
six_btn.grid(row=4, column=2, padx=3, pady=3)

multi_btn = Button(window, text='×', width=7, height=2, bg='Light Grey', command=lambda: btn_press('*'))
multi_btn.grid(row=4, column=3, padx=3, pady=3)

one_btn = Button(window, text='1', width=7, height=2, bg='Grey', command=lambda: btn_press('1'))
one_btn.grid(row=5, column=0, padx=3, pady=3)

two_btn = Button(window, text='2', width=7, height=2, bg='Grey', command=lambda: btn_press('2'))
two_btn.grid(row=5, column=1, padx=3, pady=3)

three_btn = Button(window, text='3', width=7, height=2, bg='Grey', command=lambda: btn_press('3'))
three_btn.grid(row=5, column=2, padx=3, pady=3)

minus_btn = Button(window, text='-', width=7, height=2, bg='Light Grey', command=lambda: btn_press('-'))
minus_btn.grid(row=5, column=3, padx=3, pady=3)

zero_btn = Button(window, text='0', width=7, height=2, bg='Grey', command=lambda: btn_press('0'))
zero_btn.grid(row=6, column=0, padx=3, pady=3)

deci_btn = Button(window, text='.', width=7, height=2, bg='Grey', command=lambda: btn_press('.'))
deci_btn.grid(row=6, column=1, padx=3, pady=3)

equal_btn = Button(window, text='=', width=7, height=2, bg='Light Blue', command=lambda: equal_press('='))
equal_btn.grid(row=6, column=2, padx=3, pady=3)

plus_btn = Button(window, text='+', width=7, height=2, bg='Light Grey', command=lambda: btn_press('+'))
plus_btn.grid(row=6, column=3, padx=3, pady=3)

frame_box = Frame(window, height=7, width=5)
frame_box.grid(row=0, columnspan=4)

entry_box = Entry(frame_box, justify=RIGHT, font=('Helvetica', 15), textvariable=entry)
entry_box.grid(row=0, columnspan=4, padx=10, pady=4)


window.mainloop()
