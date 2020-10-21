from python_code.methods.equation import dichotomy, hords, tangent_newton, iterations
from python_code.staf.sympy_init import Float

# ==========================================================================
# Нахождение корней уравнения методом дихотомии, хорд, касательных, итераций
# ==========================================================================


# Введите данные из задания
task = {
    'Функция для метода дихотоми': '2 * x * x * x + 5 * x - 1.6',
    'Отрезок для метода дихотомии': (0, 1),
    'Функция для метода хорд': 'x * x * x + 9 * x + 5',
    'Отрезок для метода хорд': (-1, 0),
    'Функция для метода касательных': '0.5 * x * x * x + 4 * x - 5',
    'Отрезок для метода касательных': (1, 2),
    'Функция для метода итераций': '4 * x ** 3 + 5 * x + 14',
    # Если вас не устраивает через какое значение был подсчитан результат - укажите два одинаковых
    'Отрезок для метода итераций': (-2, -1),
    'x = g(x)': None
}

# Данные из методички для проверки работы программы (проверьте - значения совпадают)
# task = {
#     'Функция для метода дихотоми': 'x * x - 2',
#     'Отрезок для метода дихотомии': (0, 8),
#     'Функция для метода хорд': 'x * x - 2',
#     'Отрезок для метода хорд': (0, 8),
#     'Функция для метода касательных': 'x * x - 2',
#     'Отрезок для метода касательных': (0, 8),
#     'Функция для метода итераций': 'x ** 3 - x ** 2 + x - 5',
#     'Отрезок для метода итераций': (0, 8),
# }

# ============================================================
# ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
# ATTENTION!  Not for timid people! Below is the program code!
# ============================================================


def print_data(data):
    step_info = ''
    for info in data:
        if 'Решение' in data.keys():
            step_info += f'{info}: {round(data[info], 8) if isinstance(data[info], float) else data[info]}\n'
        elif 'Номер итерации' in data.keys():
            value = data[info]
            if isinstance(value, float):
                value = round(value, 8)
            elif isinstance(value, Float):
                value = round(float(value), 8)
            step_info += f'{info}: {value}'.center(23) + '|'
        else:
            step_info += f'{info}:\n{round(data[info], 8) if isinstance(data[info], float) else data[info]}\n'
    if 'Решение' in data.keys():
        print('\n')
    elif 'Номер итерации' in data.keys():
        print(('-' * 23 + '+') * len(data.keys()))
    print(step_info)


try:
    print(' Решение методом дихотомии '.center(100, '='))
    decision = dichotomy(task['Функция для метода дихотоми'], task['Отрезок для метода дихотомии'],
                         iterations=5, accuracy_order=3, level_of_details=2)
    for step in decision:
        print_data(step)

    print(' Решение методом хорд '.center(100, '='))
    decision = hords(task['Функция для метода хорд'], task['Отрезок для метода хорд'],
                     iterations=5, accuracy_order=3, level_of_details=2)
    for step in decision:
        print_data(step)

    print(' Решение методом касательных '.center(100, '='))
    decision = tangent_newton(task['Функция для метода касательных'], task['Отрезок для метода касательных'],
                              iterations=5, accuracy_order=3, level_of_details=2)
    for step in decision:
        print_data(step)

    print(' Решение методом итераций '.center(100, '='))
    decision = iterations(task['Функция для метода итераций'], task['Отрезок для метода итераций'], task.get('x = g(x)'),
                          level_of_details=2, iterations=5, accuracy_order=3)
    for step in decision:
        if "g'(x)" in step.keys():
            step.update({"g'(x)": None})
        print_data(step)

except Exception as error:
    print(error)

input('\nНажмите "Enter" чтобы выйти...')
