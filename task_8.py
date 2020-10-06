from python_code.methods.interpol.lagrange import lagrange_pol
from python_code.methods.interpol.newton import newton_pol
from python_code.methods.interpol.canonical import canonical_pol

# =================================================================================
# Нахождение интерполяция методами Лагранжа, Ньютона и через канонический многочлен
# =================================================================================

try:
    table_for_lagrange = {
        'x': [2, 3, 4],
        'y': [20, 22, 19],
        'Подставить значения': [3.5]
    }

    table_for_newton = {
        'x': [3, 4, 5],
        'y': [22, 19, 18],
        'Подставить значения': [3.5]
    }

    table_for_canonical = {
        'x': [2, 3, 4, 5],
        'y': [20, 22, 19, 18],
        'Подставить значения': [3.5],
        'Рисовать график?': 'да'
    }

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================

    print(' Многочлен Лагранжа '.center(100, '='))

    lagrange_result = lagrange_pol(table_for_lagrange['x'], table_for_lagrange['y'])
    print(f'Полный многочлен: {lagrange_result["Полный многочлен"]}\n'
          f'Упрощенный многочлен: {lagrange_result["Упрощенный многочлен"]}')
    function = lagrange_result['Функция python']
    for val in table_for_lagrange['Подставить значения']:
        print(f'y({val}) = {round(function(val), 8)}')

    print(' Многочлен Ньютона '.center(100, '='))

    lagrange_result = newton_pol(table_for_newton['x'], table_for_newton['y'])
    print(f'Полный многочлен: {lagrange_result["Полный многочлен"]}\n'
          f'Упрощенный многочлен: {lagrange_result["Упрощенный многочлен"]}')
    function = lagrange_result['Функция python']
    for val in table_for_newton['Подставить значения']:
        print(f'y({val}) = {round(function(val), 8)}')

    print(' Канонический многочлен '.center(100, '='))

    canonical_result = canonical_pol(table_for_canonical['x'], table_for_canonical['y'])
    print('Матрица:')
    canonical_result['Матрица'].console_display()
    print(f'Столбец свободных членов: {canonical_result["Столбец свободных членов"]}\n')
    print(f'Решение СЛАУ: {canonical_result["Решение СЛАУ"]}')
    print(f'Полином: {canonical_result["Полином"]}\n')
    function = canonical_result['Функция python']
    for val in table_for_canonical['Подставить значения']:
        print(f'y({val}) = {round(function(val), 8)}')
    if table_for_canonical['Рисовать график?'].lower() == 'да':
        print('\n', " Увы, график рисовать я пока не умею ".center(50, '!'))

except Exception as error:
    print(error)

input('\nНажмите "Enter" чтобы выйти...')
