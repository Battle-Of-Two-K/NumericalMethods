from tkinter import *

root = Tk()
root.resizable(False, False)
root.title("Переписывавйте уравнения правильно!")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Label(text="Функция для метода дихотоми:", font=('Arial', 32)).grid(row=0, column=0, pady=10)
input_box_1 = Entry(width=30, font=('Arial', 32))
input_box_1.grid(row=0, column=1, columnspan=3, pady=10)
#------------------------------------------------------------------
Label(text="Отрезок для метода дихотомии:", font=('Arial', 32)).grid(row=1, column=0, pady=10)
first_value_1 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', 32))
first_value_1.delete(0, END)
first_value_1.insert(0, '0')
first_value_1.grid(row=1, column=1)
#------------------------------------------------------------------
Label(text=";", font=('Arial', 32)).grid(row=1, column=2, pady=10)
second_value_1 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', 32))
second_value_1.delete(0, END)
second_value_1.insert(0, '0')
second_value_1.grid(row=1, column=3, pady=10)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Label(text="Функция для метода хорд:", font=('Arial', 32)).grid(row=3, column=0, pady=10)
input_box_2 = Entry(width=30, font=('Arial', 32))
input_box_2.grid(row=3, column=1, columnspan=3, pady=10)
#------------------------------------------------------------------
Label(text="Отрезок для метода хорд:", font=('Arial', 32)).grid(row=4, column=0, pady=10)
first_value_2 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', 32))
first_value_2.delete(0, END)
first_value_2.insert(0, '0')
first_value_2.grid(row=4, column=1, pady=10)
#------------------------------------------------------------------
Label(text=";", font=('Arial', 32)).grid(row=4, column=2, pady=10)
second_value_2 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', 32))
second_value_2.delete(0, END)
second_value_2.insert(0, '0')
second_value_2.grid(row=4, column=3, pady=10)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Label(text="Функция для метода касательных:", font=('Arial', 32)).grid(row=6, column=0, pady=10)
input_box_3 = Entry(width=30, font=('Arial', 32))
input_box_3.grid(row=6, column=1, columnspan=3, pady=10)
#------------------------------------------------------------------
Label(text="Отрезок для метода касательных:", font=('Arial', 32)).grid(row=7, column=0, pady=10)
first_value_3 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', 32))
first_value_3.delete(0, END)
first_value_3.insert(0, '0')
first_value_3.grid(row=7, column=1, pady=10)
#------------------------------------------------------------------
Label(text=";", font=('Arial', 32)).grid(row=7, column=2, pady=10)
second_value_3 = Spinbox(width=6, values=tuple(range(-100, 100)), font=('Arial', 32))
second_value_3.delete(0, END)
second_value_3.insert(0, '0')
second_value_3.grid(row=7, column=3, pady=10)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Label(text="Функция для метода итераций:", font=('Arial', 32)).grid(row=9, column=0, pady=10)
input_box_4 = Entry(width=30, font=('Arial', 32))
input_box_4.grid(row=9, column=1, columnspan=3, pady=10)
#------------------------------------------------------------------
Label(text="Отрезок для метода итераций:", font=('Arial', 32)).grid(row=10, column=0, pady=10)
first_value_4 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', 32))
first_value_4.delete(0, END)
first_value_4.insert(0, '0')
first_value_4.grid(row=10, column=1, pady=10)
#------------------------------------------------------------------
Label(text=";", font=('Arial', 32)).grid(row=10, column=2, pady=10)
second_value_4 = Spinbox(width=6, values=tuple(range(-100, 100)), font=('Arial', 32))
second_value_4.delete(0, END)
second_value_4.insert(0, '0')
second_value_4.grid(row=10, column=3, pady=10)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Button(text="Посчитать", font=('Arial', 32)).grid(row=11, column=1, columnspan=3, pady=20)

root.mainloop()
