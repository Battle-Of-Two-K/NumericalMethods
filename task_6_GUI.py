from tkinter import *

from python_code.methods.equation import dichotomy, hords, tangent_newton, iterations

__author__ = 'Battle-Of-Two-K'

all_font_size = 16

root = Tk()
root.resizable(False, False)
root.title("Переписывавйте уравнения правильно!")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Label(text="Функция для метода дихотоми:", font=('Arial', all_font_size)).grid(row=0, column=0, pady=10)
input_box_1 = Entry(width=30, font=('Arial', all_font_size))
input_box_1.grid(row=0, column=1, columnspan=3, pady=10)
# ------------------------------------------------------------------
Label(text="Отрезок для метода дихотомии:", font=('Arial', all_font_size)).grid(row=1, column=0, pady=10)
first_value_1 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', all_font_size))
first_value_1.delete(0, END)
first_value_1.insert(0, '0')
first_value_1.grid(row=1, column=1)
# ------------------------------------------------------------------
Label(text=";", font=('Arial', all_font_size)).grid(row=1, column=2, pady=10)
second_value_1 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', all_font_size))
second_value_1.delete(0, END)
second_value_1.insert(0, '0')
second_value_1.grid(row=1, column=3, pady=10)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Label(text="Функция для метода хорд:", font=('Arial', all_font_size)).grid(row=3, column=0, pady=10)
input_box_2 = Entry(width=30, font=('Arial', all_font_size))
input_box_2.grid(row=3, column=1, columnspan=3, pady=10)
# ------------------------------------------------------------------
Label(text="Отрезок для метода хорд:", font=('Arial', all_font_size)).grid(row=4, column=0, pady=10)
first_value_2 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', all_font_size))
first_value_2.delete(0, END)
first_value_2.insert(0, '0')
first_value_2.grid(row=4, column=1, pady=10)
# ------------------------------------------------------------------
Label(text=";", font=('Arial', all_font_size)).grid(row=4, column=2, pady=10)
second_value_2 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', all_font_size))
second_value_2.delete(0, END)
second_value_2.insert(0, '0')
second_value_2.grid(row=4, column=3, pady=10)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Label(text="Функция для метода касательных:", font=('Arial', all_font_size)).grid(row=6, column=0, pady=10)
input_box_3 = Entry(width=30, font=('Arial', all_font_size))
input_box_3.grid(row=6, column=1, columnspan=3, pady=10)
# ------------------------------------------------------------------
Label(text="Отрезок для метода касательных:", font=('Arial', all_font_size)).grid(row=7, column=0, pady=10)
first_value_3 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', all_font_size))
first_value_3.delete(0, END)
first_value_3.insert(0, '0')
first_value_3.grid(row=7, column=1, pady=10)
# ------------------------------------------------------------------
Label(text=";", font=('Arial', all_font_size)).grid(row=7, column=2, pady=10)
second_value_3 = Spinbox(width=6, values=tuple(range(-100, 100)), font=('Arial', all_font_size))
second_value_3.delete(0, END)
second_value_3.insert(0, '0')
second_value_3.grid(row=7, column=3, pady=10)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Label(text="Функция для метода итераций:", font=('Arial', all_font_size)).grid(row=9, column=0, pady=10)
input_box_4 = Entry(width=30, font=('Arial', all_font_size))
input_box_4.grid(row=9, column=1, columnspan=3, pady=10)
# ------------------------------------------------------------------
Label(text="Отрезок для метода итераций:", font=('Arial', all_font_size)).grid(row=10, column=0, pady=10)
first_value_4 = Spinbox(width=7, values=tuple(range(-100, 100)), font=('Arial', all_font_size))
first_value_4.delete(0, END)
first_value_4.insert(0, '0')
first_value_4.grid(row=10, column=1, pady=10)
# ------------------------------------------------------------------
Label(text=";", font=('Arial', all_font_size)).grid(row=10, column=2, pady=10)
second_value_4 = Spinbox(width=6, values=tuple(range(-100, 100)), font=('Arial', all_font_size))
second_value_4.delete(0, END)
second_value_4.insert(0, '0')
second_value_4.grid(row=10, column=3, pady=10)


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def knopka():
    def print_data(data):
        step_info = ''
        for info in data:
            if 'Решение' in data.keys():
                step_info += f'{info}: {round(data[info], 8) if isinstance(data[info], float) else data[info]}\n'
            elif 'Номер итерации' in data.keys():
                step_info += f'{info}: ' \
                             f'{round(data[info], 8) if isinstance(data[info], float) else data[info]}'.center(23) + '|'
            else:
                step_info += f'{info}:\n{round(data[info], 8) if isinstance(data[info], float) else data[info]}\n'
        if 'Решение' in data.keys():
            print('\n')
        elif 'Номер итерации' in data.keys():
            print(('-' * 23 + '+') * len(data.keys()))
        print(step_info)

    print(' Решение методом дихотомии '.center(100, '='))
    decision = dichotomy(input_box_1.get(),
                         (float(first_value_1.get()),
                          float(second_value_1.get())),
                         iterations=5, accuracy_order=3, level_of_details=2)
    for step in decision:
        print_data(step)

    print(' Решение методом хорд '.center(100, '='))
    decision = hords(input_box_2.get(),
                     (float(first_value_2.get()),
                      float(second_value_2.get())),
                     iterations=5, accuracy_order=3, level_of_details=2)
    for step in decision:
        print_data(step)

    print(' Решение методом касательных '.center(100, '='))
    decision = tangent_newton(input_box_3.get(),
                              (float(first_value_3.get()),
                               float(second_value_3.get())),
                              iterations=5, accuracy_order=3, level_of_details=2)
    for step in decision:
        print_data(step)

    print(' Решение методом итераций '.center(100, '='))
    decision = iterations(input_box_4.get(),
                          (float(first_value_4.get()),
                           float(second_value_4.get())),
                          level_of_details=2, iterations=5, accuracy_order=3)
    for step in decision:
        print_data(step)


calculation_button = Button(text="Посчитать", font=('Arial', all_font_size))
calculation_button.grid(row=11, column=1, columnspan=3, pady=20)

calculation_button.config(command=knopka)

root.mainloop()
