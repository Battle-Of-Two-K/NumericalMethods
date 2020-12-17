from python_code.methods.integrate.trapezoid import trapezoid_integral
from python_code.methods.integrate.simpson import simpson_integral
from python_code.staf.sympy_init import *


# ============================================
# Численное интегрирование по формуле трапеций
# ============================================


def main():
    function = 'sin(x)'  # интегрируемая функция
    section = (0, pi / 2)  # пределы интегрирования
    number_of_steps = 4  # количество шагов

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================

    def print_data(data):
        step_info = ''
        for info in data:
            if isinstance(data[info], (tuple, list)):
                step_info += f'{info}: {list(map(lambda val: round(float(val), 8), step[info]))}\n'
            elif isinstance(data[info], float):
                step_info += f'{info}: {round(data[info], 8)}\n'
            else:
                step_info += f'{info}: {data[info]}\n'
        print(step_info)

    print(' Численное интегрирование по формуле трапеций '.center(75, '='))
    decision = trapezoid_integral(function, section, number_of_steps, level_of_details=1)
    for step in decision:
        print_data(step)

    decision = simpson_integral(function, section, number_of_steps, level_of_details=1)
    for step in decision:
        print_data(step)


if __name__ == '__main__':
    # Файлы task_%.py сделаны для людей, для которых установка интерпретатора может стать испытанием.
    # Запускают эти люди двойными кликом. А если перед ними консоль будет мгновенно закрываться в случае ошибки,
    # это будет жуткий стресс, а я даже помочь быстро не смогу, а так хоть print ошибки есть.
    try:
        main()
    except Exception as error:
        print(error)
    input('Нажмите "Enter" чтобы выйти...')
